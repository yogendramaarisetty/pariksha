from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from . import forms, views
from django.conf.urls import url
from .forms import UserLoginForm

urlpatterns = [
    
    
    path('register/',views.pariksha_register,name='register'),
    path(r'^account_activation_sent/$',views.account_activation_sent,name='account_activation_sent'),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate,name='activate'),
    path('loggedout/',auth_views.LogoutView.as_view(template_name="challenge/home.html"),name="logout"),
    path('tests_available/',views.challenges,name='tests'),
    url(r'^challenge/testpage/(?P<challenge_id>\d+)/(?P<c_id>\d+)/$',views.testpage,name='testpage'),
    url(r'^challenge/testpage/(?P<challenge_id>\d+)/(?P<c_id>\d+)/submitted$',views.submittedpage,name='submittedpage'),
    url(r'^challenge/testpage/completedTest$',views.completed_testpage,name='completed_testpage'),
    url(r'^candidate_form/testInstruction/(?P<pk>\d+)/(?P<c_id>\d+)/$', views.test_instruction, name='test_instruction'),
    url(r'^candidate_form/(?P<challenge_id>\d+)/$', views.candidate_form, name='candidate_form'),
    path('login/',auth_views.LoginView.as_view( template_name="challenge/login.html",authentication_form=UserLoginForm),name="login"),
    path('question_bank/',views.question_bank,name="question_bank"),
    path('questioncreate/',views.QuestionCreate.as_view(),name="question_create"),
    path('create_Contest/',views.create_contest_form,name="create_contest"),
    # path('question_bank/<q_id>/view/',views.question_view(),name="question_edit"),
    path(r'challenge/testpage/(?P<challenge_id>\d+)/(?P<u_id>\d+)/compile_run/',views.compile_run,name='compile_run'),
    path('admin_management/',views.admin_management,name='admin_manage'),

]