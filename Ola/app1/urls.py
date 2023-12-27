from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # path("contact/<str:name>/<str:place>/<int:age>", views.contact, name="contact")
    path("contact", views.contact, name="contact"),
    path("formview", views.formview, name='formview')
]