from django.urls import path
from . import views

urlpatterns = [
    path('temptomod1/', views.empview, name="temptomod")
]