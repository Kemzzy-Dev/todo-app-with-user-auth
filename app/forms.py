from django import forms
from .models import Todo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'mb-3 form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'mb-3 form-control', 'placeholder':'Username'}),
            'email': forms.EmailInput(attrs={'class': 'mb-3 form-control', 'placeholder':'Email'}),
        }

class LoginUserForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())



class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task', 'is_completed']
        widgets = {
            'task': forms.TextInput(attrs={'class': 'mt-2 rounded-0 form-control', 'placeholder':'Enter Task'})
        }