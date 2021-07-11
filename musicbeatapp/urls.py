from django.urls import path,include
from . import views


urlpatterns = [
    path("songs/", views.songs, name = 'songs'),
    path("songs/<int:id>", views.songpost, name = 'songpost'),
    path("login" , views.login, name  = 'login'),
    path("signup" , views.signup, name  = 'signup'),
    path('demo', views.demo, name = 'demo'),
    path("errorthis" , views.errorthis, name = 'errorthis'),
    path("logout" , views.handleLogout, name  = 'handleLogout'),
    path("search" , views.search, name  = 'search'),
] 

