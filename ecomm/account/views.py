from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserSigninForm
from django.contrib.auth import login, logout, authenticate
from django.views.generic import CreateView, FormView, TemplateView


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
            return render(request, self.template_name, {"form":self.form_class})

class SignOutView(TemplateView):
    template_name = "accounts/signout.html"
    success_url = "/"
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, 'accounts/signout.html')