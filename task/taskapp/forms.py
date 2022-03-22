from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class Registerform(UserCreationForm):
    class Meta:
        model= User
        fields = ['username', 'email']
        labels = {'email': 'Email'}


class EditForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'email', 'date_joined', 'last_login']
        labels = {'email': 'Email'}


class EditAdminForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = '__all__'
        labels = {'email': 'Email'}

