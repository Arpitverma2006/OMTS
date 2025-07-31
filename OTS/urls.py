from django.urls import path
from OTS.views import *
from . import views
app_name='OTS'
urlpatterns =[
    path('',welcome),
    path('new-candidate',candidateRegistrationForm, name='registrationForm'),
    path('store-candidate',candidateRegistration,name='storeregistration'),
    path('login',loginView,name='login'),
    path('home',candidateHome,name='home'),
    path('test-paper',testPaper,name='testPaper'),
    path('calculate-result',calculateTestResult,name='calculateTestResult'),
    path('test-history',testResultHistory,name='testHistory'),
    path('result',showTestResult,name='result'),
    path('logout',logoutView,name='logout'),
    # path('result/', views.showResult, name='result'),  # <- Add this line
    # path('calculate-result/', views.calculateTestResult, name='calculate-result'),
]