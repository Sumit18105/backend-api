from django.urls import path
from . import views

urlpatterns = [
    path('create-user/', views.createUser),
    path('check-user/', views.checkUser),
    path('delete-user/', views.deleteUser),
]