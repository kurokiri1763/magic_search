from django.urls import path
from .views import magic_search
from . import views

urlpatterns = [
    path('', views.magic_list, name='magic_list'),
    path('<int:magic_id>/', views.magic_detail, name='magic_detail'),
    path('search/', views.magic_search, name='magic_search'),
]