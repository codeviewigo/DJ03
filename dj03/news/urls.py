# urls.py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('news/add/', views.add_news, name='add_news'),
    path('news/<int:pk>/edit/', views.edit_news, name='edit_news'),
]
