
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [

    path('newslist/',views.NewsListView.as_view(),name='news_list'),
    path('createnews/',views.NewsCreateView.as_view(),name='news_create'),
    path('newsdetail/<int:pk>/',views.NewsDetailView.as_view(),name='news_detail'),
]
