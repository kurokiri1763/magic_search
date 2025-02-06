from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),  # ホーム画面
    path('register/', views.SignupView.as_view(), name='register'),  # ユーザー登録
    path('login/', views.LoginView.as_view(), name='login'), # ログイン画面
    path('logout/', views.LogoutView.as_view(), name='logout'), # ログアウト画面
]