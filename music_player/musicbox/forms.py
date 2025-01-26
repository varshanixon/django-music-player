from django import forms

from django.contrib.auth.forms import UserCreationForm

from musicbox.models import User



class SignUpForm(UserCreationForm):

    class Meta:

        model = User

        fields = ['username','first_name','last_name','dob','phone','email','password1','password2']


