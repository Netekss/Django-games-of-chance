from django.urls import path
from . import views

urlpatterns = [
    path('', views.level_choice, name='guessnumber_level_choice'),
    path('level-easy', views.level_easy, name='guessnumber_level_easy'),
    path('level-normal', views.level_normal, name='guessnumber_level_normal'),
    path('level-hard', views.level_hard, name='guessnumber_level_hard'),
]
