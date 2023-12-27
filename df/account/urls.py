from django.urls import path
from . import views

urlpatterns = [
    path('<name>/<age>/<place>/', views.home, name='home'),
    path('formview1/', views.formview, name="formview"),
    path('ans/', views.answer, name="answer")
]