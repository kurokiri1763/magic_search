from django.urls import path
from .views import magic_search
from . import views

app_name = 'search'

urlpatterns = [
    path('<int:magic_id>/', views.magic_detail, name='magic_detail'),
    path('', views.magic_search, name='magic_search'),
]