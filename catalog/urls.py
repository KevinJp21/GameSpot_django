from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new_platform/', views.new_platform, name='new_platform'),
    path('platform_list/', views.platform_list, name='platform_list'),
    path('update_platform/<int:id>/', views.update_platform, name='update_platform'),
]