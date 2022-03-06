from django.urls import path
from api import views


urlpatterns = [
    path('movies', views.search_movies),
    path('top_250', views.top_250),
    ]