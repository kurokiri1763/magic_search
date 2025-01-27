from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_magic, name='add_magic'),  # 魔法追加ページ
]
