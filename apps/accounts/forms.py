from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm,
)

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        