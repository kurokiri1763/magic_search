from django.urls import path
from .views import IndexView, SignupView

app_name = 'accounts'

urlpatterns = [
    path("", IndexView.as_view(), name="index"),  # ホーム画面
    path("register/", SignupView.as_view(), name="register"),  # ユーザー登録
]