from django.urls import re_path

from JobsApp import views

from django.conf import settings

urlpatterns=[
    re_path(r'^job/$', views.jobApi),
    re_path(r'^job/([0-9]+)$', views.jobApi),
]