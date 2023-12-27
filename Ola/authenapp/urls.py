from django.urls import path
from . import views

urlpatterns = [
    path('registerlink/',views.register, name="register"),
    path('login/', views.login_request, name="login_request"),
    path('logoutpage/', views.logout_user, name="logout")
]