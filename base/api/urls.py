from .import views
from django.urls import path

urlpatterns = [
    path('', views.getRouter),
    path('api/posts/', views.getPosts),
]