from django.shortcuts import render,redirect

from django.views.generic import View

from musicbox.forms import SignUpForm

# Create your views here.


class SignUpView(View):

    template_name = 'signup.html'

    form_class = SignUpForm

    def get(self,request,*args,**kwargs):

        form_instance = self.form_class

        return render(request,self.template_name,{'form':form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance = self.form_class(request.POST)

        if form_instance.is_valid():

            form_instance.save()

            return redirect('signup')
        
        return render(request,self.template_name,{'form':form_instance})
    
    