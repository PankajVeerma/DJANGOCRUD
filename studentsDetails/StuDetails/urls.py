from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('insert', views.insert, name='insert'),
    path('delete/<id>', views.deleteData, name='deleteData'),
    path('update/<id>', views.updateData, name='updateData'),
]
