from django.urls import path
from django.conf.urls import url
from . import views

##Test


# TEMPLATE TAGGING
app_name = 'Mylearning'


urlpatterns = [

    path('', views.Mylearning, name='Mylearning'),
    path('InterviewQuestion/', views.InterviewQuestion, name='InterviewQuestion'),
    path('InterviewQA/', views.InterviewQuestionAnswer, name='InterviewQuestionAnswer'),
    path(r'reg/', views.StudentReg, name='StudentReg'),

]
