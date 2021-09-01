from django import forms
from django.contrib.auth.models import User
from login_app.models import UserInfo

class  UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        exclude = ['user']
