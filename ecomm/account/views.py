from django.contrib import messages
from django.http import request
from django.shortcuts import render, redirect
from .forms import (UserRegisterForm,
                    UserSigninForm,
                    ProfileForm)
from django.contrib.auth.mixins import (LoginRequiredMixin, 
                                        UserPassesTestMixin)
from .models import Profile
from django.contrib.auth import login, logout, authenticate
from django.views.generic import (CreateView, 
                                  FormView, 
                                  TemplateView, 
                                  DetailView, 
                                  UpdateView
                                  )


class SignUpView(CreateView):
    form_class = UserRegisterForm
    template_name = "account/signup.html"
    success_url = "/"
    
    
class SignInView(FormView):
    form_class = UserSigninForm
    success_url = '/'
    template_name = "account/signin.html"
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(self.success_url)
        else:
            msg = messages.warning(request, "Incorrect Username or Password!")
            return render(request, self.template_name, {"form":self.form_class, 'message':msg})

class SignOutView(TemplateView):
    template_name = "accounts/signout.html"
    success_url = "/"
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, 'account/signout.html')
    


class ProfileView(DetailView):
    model = Profile
    form_class = ProfileForm
    template_name = "account/profile.html"
    success_url = "/"
    
class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    
    model = Profile
    template_name = "account/profileupdate.html"
    form_class = ProfileForm
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

        
    