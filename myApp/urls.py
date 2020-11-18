from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('addMovies/', views.addMovies, name='addMovies'),
    path('about/', views.about, name='about'),
    path('viewMovies', views.viewMovies, name='viewMovies'),
    path('add', views.add, name='add'),
]

