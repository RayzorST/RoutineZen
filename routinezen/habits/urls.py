from django.urls import path
from . import views

urlpatterns = [
    path('', views.habits),
    path('statistics/', views.statistics),
]