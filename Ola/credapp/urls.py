from django.urls import path
from . import views

urlpatterns = [
    path('createform/', views.createemp, name="createform"),
    path('data/', views.alldata, name="alldata"),
    path('update/<id>', views.updateemp, name='update'),
    path('delete/<id>', views.delemp, name="delete")
]