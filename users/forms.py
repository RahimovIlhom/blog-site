from django.contrib.auth.forms import UserCreationForm

from users.models import CustomUser


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'gender', 'password1', 'password2']

