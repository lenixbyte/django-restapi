from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(
        label='Password', max_length=30, widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('User with this Username already exists.')

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )
        return user
