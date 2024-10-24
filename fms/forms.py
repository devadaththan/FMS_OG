from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

from django.contrib.auth.models import User

class UserSelectionForm(forms.Form):
    users = forms.ModelChoiceField(queryset=User.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))

