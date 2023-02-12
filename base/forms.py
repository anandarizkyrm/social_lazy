from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Post


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['author', 'likes']


# class UserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['avatar', 'name', 'username', 'email', 'bio']
