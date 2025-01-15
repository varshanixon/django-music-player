from django.shortcuts import render

from django.views.generic import View

from musicbox.forms import SignUpForm

# Create your views here.


class SignUpView(View):

    template_name = 'signup.html'

    form_class = SignUpForm

    def get(self,request,*args,**kwargs):

        form_instance = self.form_class

        return render(request,self.template_name,{'form':form_instance})