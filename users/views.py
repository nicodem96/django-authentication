from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import ImageChangeForm, ModifyProfileForm
from django.views import View
# Create your views here.

@login_required
def profile(request):
    return render(request, 'users/profile.html')


class CreateProfileView(LoginRequiredMixin, View):
    def get(self, request):
        form = ModifyProfileForm()
        return render(request, "users/create_profile.html", {
            "form" : form
        })

    def post(self, request):
        submitted_form = ModifyProfileForm(instance = request.user,
                                              data = request.POST, 
                                              )
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect("profile")
        
        return render(request, "users/create_profile.html", {
            "form" : submitted_form
        })
    
class ModifyImageView(LoginRequiredMixin, View):
    def get(self, request):
        form = ImageChangeForm()
        return render(request, "users/modify_photo.html", {
            "form" : form
        })

    def post(self, request):
        submitted_form = ImageChangeForm(instance = request.user,
                                              data = request.POST, 
                                              files = request.FILES)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect("profile")
        
        return render(request, "users/modify_photo.html", {
            "form" : submitted_form
        })
