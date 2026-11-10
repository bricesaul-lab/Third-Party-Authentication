from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User

class RegistrationForm(UserCreationForm):
    # email = forms.EmailField(max_length = 60)
    # username = forms.CharField(max_length=10)
    fname = forms.CharField(
        max_length= 30, 
        label= 'First Name',
        widget= forms.TextInput(attrs= { 'class' : 'form-control'}), 
        required= True)
    
    lname = forms.CharField(
        max_length=10, 
        label= 'Last Name', 
        widget= forms.TextInput(attrs= { 'class' : 'form-control'}), 
        required = True)

    password1 = forms.CharField(
        help_text=None,
        widget= forms.PasswordInput(attrs= { 'class' : 'form-control', 'type' : 'password'}),
        label= 'Password',
        required = True
        )

    password2 = forms.CharField(
        help_text=None,
        widget= forms.PasswordInput(attrs= { 'class' : 'form-control', 'type' : 'password'}),
        label= 'Confirm Password'
        )
        



    class Meta:
        model = User
        fields = ['email','username','fname','lname','password1','password2']

        widgets = {
            'email'     : forms.EmailInput(attrs= { 'class' : 'form-control'}),
            'username'  : forms.TextInput(attrs= { 'class' : 'form-control'}),
        }

