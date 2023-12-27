from django.urls import path
from . import views

urlpatterns = [
    path('charcount/', views.charcounterview, name="charcount")
]