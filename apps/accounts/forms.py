from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm,
)


class SignupForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "nickname",
            "email",
        )
        labels = {
            "username": "아이디",
            "nickname": "이름",
            "email": "이메일",
        }
