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
    path('loggedout/',auth_views.LogoutView.as_view(template_name="challenge/home.html"),name="logout"),
    path('tests_available/',views.challenges,name='tests'),
    url(r'^contest/testpage/(?P<challenge_id>\d+)/(?P<c_id>\d+)/$',views.testpage,name='testpage'),
    url(r'^contest/testpage/(?P<challenge_id>\d+)/(?P<c_id>\d+)/submitted$',views.submittedpage,name='submittedpage'),
    url(r'^contest/testpage/(?P<challenge_id>\d+)/(?P<c_id>\d+)/completedTest$',views.completed_testpage,name='completed_testpage'),
    url(r'^candidate_form/testInstruction/(?P<pk>\d+)/(?P<c_id>\d+)/$', views.test_instruction, name='test_instruction'),
    url(r'^candidate_form/(?P<challenge_id>\d+)/$', views.candidate_form, name='candidate_form'),
   url(r'^contest_management/$', views.manage_contests , name='manage_contests'),
    path('login/',auth_views.LoginView.as_view( template_name="challenge/login.html",authentication_form=UserLoginForm),name="login"),
    path('question_bank/',views.question_bank,name="question_bank"),
    path('demoIDE/',views.demo_ide,name="demo_ide"),
    path('contact/',views.contact,name="contact"),
    path('Results/',views.results,name="results"),
    url(r'^contest_Results/(?P<contest_id>\d+)/$', views.contest_results, name='contest_results'),
    url(r'^download_Results/(?P<contest_id>\d+)/$', views.download_result, name='download_result'),
    path('create_Question/',views.create_question_form,name="create_question"),
    # url(r'^modify/(?P<question_id>\d+)/question$', views.question_edit_form, name='question_edit_form'),
    
    path('create_Contest/',views.create_contest_form,name="create_contest"),
    url(r'^modify/(?P<contest_id>\d+)/contest$', views.contest_edit_form, name='contest_edit_form'),
    url(r'^modify/(?P<question_id>\d+)/question$', views.question_edit_form, name='question_edit_form'),
    # path('question_bank/<q_id>/view/',views.question_view(),name="question_edit"),
    path(r'challenge/testpage/(?P<challenge_id>\d+)/(?P<u_id>\d+)/compile_run/',views.compile_run,name='compile_run'),
    path('admin_management/',views.admin_management,name='admin_manage'),
    path('testpage/',views.temp_testpage_design,name='testpage_design'),
    path('process_submission/',views.run_all_test_submissions,name='process_submission')

]