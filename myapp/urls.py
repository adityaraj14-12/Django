from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('vote/', views.vote, name='vote'),
    path('', views.home, name='home'),
]
