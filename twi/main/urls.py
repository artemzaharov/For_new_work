from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='news_list'),
    path('sorted/', views.sort, name='sort_list'),
]
