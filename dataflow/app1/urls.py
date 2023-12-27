from django.urls import path
from . import views

urlpatterns = [
    path('<name>/<age>/<place>', views.home, name="home"),
    # path('', views.home, name="home"),
    path("show", views.show, name="show")
]