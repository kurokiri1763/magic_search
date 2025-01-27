from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """
    カスタムユーザー登録フォーム
    """
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'icon')

class CustomUserChangeForm(UserChangeForm):
    """
    カスタムユーザー情報変更フォーム
    """
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'icon')

class CustomAuthenticationForm(AuthenticationForm):
    """
    認証フォームをカスタマイズする場合、このクラスを利用
    """
    pass
