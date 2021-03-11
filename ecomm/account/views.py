from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
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
                                  UpdateView,
                                  ListView
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
        messages.success(request, "You are successfully logged out!")
        return redirect('/')
    
class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "account/profile.html"
    success_url = "/"

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "ecommpage/create.html"
    success_url = '/'
        
class StaffListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'account/staff.html'