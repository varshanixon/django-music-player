from django import forms

from django.contrib.auth.forms import UserCreationForm

from musicbox.models import User



class SignUpForm(UserCreationForm):

    class Meta:

        model = User

        fields = ['username','first_name','last_name','dob','phone','email','password1','password2']

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control mb-2'}),

            'first_name': forms.TextInput(attrs={'class':'form-control mb-2'}),
            
            'last_name': forms.TextInput(attrs={'class':'form-control mb-2'}),
            
            'dob': forms.DateInput(attrs={'class':'form-control mb-2','type':'date'}),
            
            'phone': forms.TextInput(attrs={'class':'form-control mb-2'}),
            
            'email': forms.EmailInput(attrs={'class':'form-control mb-2'}),
            
            'password1': forms.PasswordInput(attrs={'class':'form-control mb-2'}),
            
            'password2': forms.PasswordInput(attrs={'class':'form-control mb-2'}),
            
        }

