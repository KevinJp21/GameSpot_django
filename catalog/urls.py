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
    path('update_genre/<int:id>/', views.update_genre, name='update_genre'),
    path('delete_genre/<int:id>/', views.delete_genre, name='delete_genre'),

    #CRUD de Desarrolladores
    path('new_developer/', views.new_developer, name='new_developer'),
    path('developer_list/', views.developer_list, name='developer_list'),
    path('update_developer/<int:id>/', views.update_developer, name='update_developer'),
    path('delete_developer/<int:id>/', views.delete_developer, name='delete_developer'),

    #CRUD de Juegos
    path('new_game/', views.new_game, name='new_game'),
    path('game_list/', views.game_list, name='game_list'),
    path('update_game/<int:id>/', views.update_game, name='update_game'),
    path('delete_game/<int:id>/', views.delete_game, name='delete_game'),
]