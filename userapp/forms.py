from django import forms
from django.forms import fields
from main.models import CustomUser
# from django.contrib.auth.models import User

class SigninForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        labels = {'username': '이름', 'password': '비밀번호'}

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'nickname', 'profile_image']
        labels = {'username': '이름', 'password': '비밀번호', 'email': '이메일', 'nickname': '닉네임', 'profile_image': '프로필 사진'}

