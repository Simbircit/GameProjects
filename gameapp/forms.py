from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class CreateUser(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['avatar']


class LoginUser(AuthenticationForm):

    class Meta:

        model = User
        fields = ['username', 'password']


class CommentForm(forms.ModelForm):

    class Meta:

        model = Comment
        fields = ['text']


class GameForm(forms.ModelForm):

    class Meta:

        model = GamePage
        fields = ['name', 'description', 'image', 'genre']
        widgets = {
            'genre': forms.CheckboxSelectMultiple(),
        }


class AddImageForm(forms.ModelForm):

    class Meta:

        model = GamePhoto
        fields = ['image']


class AddFileForm(forms.ModelForm):

    class Meta:

        model = GameFile
        fields = ['file']


class DeleteImageForm(forms.ModelForm):
    class Meta:
        model = GamePhoto
        fields = ['image']
