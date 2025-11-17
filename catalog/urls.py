from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new_platform/', views.new_platform, name='new_platform'),
    path('platform_list/', views.platform_list, name='platform_list'),
]