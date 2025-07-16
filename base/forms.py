from django.forms import ModelForm
from .models import Post, customUser
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class PostForm(ModelForm):
    class Meta:
        model= Post
        fields= ['text', 'image']


class RegisterForm(UserCreationForm):
    class Meta:
        model= customUser
        fields= ['name', 'username', 'email', 'bio', 'avatar', 'password1', 'password2']


class EditUserForm(UserCreationForm):
    class Meta:
        model= customUser
        fields= ['name', 'email', 'bio', 'avatar', 'password1', 'password2']