from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserChangeForm, ImageChangeForm
from django.views import View
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account creato per {username}")
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {
        "form" : form
    })

class MyLoginView(LoginView):
    template_name = 'users/login.html'
    next_page = 'home'

class MyLogoutView(LogoutView):
    template_name = 'users/logout.html'


@login_required
def profile(request):
    return render(request, 'users/profile.html')



class CreateProfileView(LoginRequiredMixin, View):
    def get(self, request):
        form = ImageChangeForm()
        return render(request, "users/create_profile.html", {
            "form" : form
        })

    def post(self, request):
        submitted_form = ImageChangeForm(instance = request.user,
                                              data = request.POST, 
                                              files = request.FILES)

        if submitted_form.is_valid():
            submitted_form.save()
            return redirect("profile")
        
        return render(request, "users/create_profile.html", {
            "form" : submitted_form
        })
