from . import views
from django.urls import path

urlpatterns=[
    path('showdetails/', views.viewdetails, name="showdetails")
]