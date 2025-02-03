from django.urls import path
from .views import edit_magic

urlpatterns = [
    path('<int:magic_id>/', edit_magic, name='edit_magic'),
]