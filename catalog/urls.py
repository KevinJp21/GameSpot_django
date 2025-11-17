from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    #CRUD de Plataformas
    path('new_platform/', views.new_platform, name='new_platform'),
    path('platform_list/', views.platform_list, name='platform_list'),
    path('update_platform/<int:id>/', views.update_platform, name='update_platform'),
    path('delete_platform/<int:id>/', views.delete_platform, name='delete_platform'),

    #CRUD de Generos
    path('new_genre/', views.new_genre, name='new_genre'),
    path('genre_list/', views.genre_list, name='genre_list'),
]