from django.urls import path
from . import views

urlpatterns = [
    path('', views.account),
    path('login/', views.LoginFormView.as_view()),
    path('registration/', views.RegistrationFormView.as_view()),
    path('me=<int:pk>', views.MeDetailView.as_view()),
]