from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='mainwebsite_index'),
    # user authentication
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    # funds
    path('add-funds/', views.add_funds, name='add_funds'),
    path('deposit/<int:amount>', views.deposit, name='deposit'),
    path('complete-deposit/', views.deposit_complete, name='complete_deposit')
]