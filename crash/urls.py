from django.urls import path
from . import views

urlpatterns = [
    path('', views.crash_bet, name='crash_bet'),
    path('play/', views.crash_game, name='crash_play'),
    path('take-money/', views.take_money, name='take_money'),
]
