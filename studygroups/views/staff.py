import datetime
import json
import unicodecsv as csv

from django import http
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext as _
from django.views.generic.base import View
from django.views.generic import ListView


from studygroups.models import Application
from ..decorators import user_is_staff

@method_decorator(user_is_staff, name='dispatch')
class ExportSignupsView(ListView):

    def get_queryset(self):
        return Application.objects.all().prefetch_related('study_group', 'study_group__course')


    def csv(self, **kwargs):
        response = http.HttpResponse(content_type="text/csv")
        response['Content-Disposition'] = 'attachment; filename="signups.csv"'
        signup_questions = ['support', 'goals', 'computer_access']
        field_names = ['study group id', 'course', 'location', 'name', 'email', 'mobile', 'date'] + signup_questions + ['use_internet']
        writer = csv.writer(response)
        writer.writerow(field_names)
        for signup in self.object_list:
            signup_data = json.loads(signup.signup_questions)
            digital_literacy = 'n/a'
            if signup_data.get('use_internet'):
                digital_literacy = dict(Application.DIGITAL_LITERACY_CHOICES)[signup_data.get('use_internet')]
            writer.writerow(
                [
                    signup.study_group_id,
                    signup.study_group.course.title,
                    signup.study_group.venue_name,
                    signup.name,
                    signup.email,
                    signup.mobile,
                    signup.created_at,
                ] + 
                [ signup_data.get(key, 'n/a') for key in signup_questions ] +
                [ digital_literacy ]
            )
        return response


    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return self.csv(**kwargs)


@method_decorator(user_is_staff, name='dispatch')
class ExportFacilitatorsView(ListView):

    def get_queryset(self):
        return User.objects.all().prefetch_related('studygroup_set', 'studygroup_set__course')


    def csv(self, **kwargs):
        response = http.HttpResponse(content_type="text/csv")
        response['Content-Disposition'] = 'attachment; filename="signups.csv"'
        field_names = ['name', 'email', 'date joined', 'last login', 'learning circles run', 'last learning circle data', 'last learning circle course', 'last learning circle venue']
        writer = csv.writer(response)
        writer.writerow(field_names)
        for user in self.object_list:
            data = [
                ' '.join([user.first_name ,user.last_name]),
                user.email,
                user.date_joined,
                user.last_login,
                user.studygroup_set.active().count()
            ] 
            last_study_group = user.studygroup_set.active().order_by('start_date').last()
            if last_study_group:
                data += [
                    last_study_group.start_date, 
                    last_study_group.course.title,
                    last_study_group.venue_name
                ]
            else:
                data += ['', '', '']
            writer.writerow(data)
        return response


    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return self.csv(**kwargs)


