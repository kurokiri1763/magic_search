from django.contrib.auth.forms import UserCreationForm ,  AuthenticationForm

from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "account_id",
            "account_name",
            "email",
            # "birth_date",
        )

class LoginForm(AuthenticationForm):
    class Meta:
        model = User