from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.generic import DeleteView
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from .forms import RegistrationFrom, LoginForm

class RegistrationFormView(FormView):
    template_name = "main\\registration.html"
    form_class = RegistrationFrom
    success_url = "/account/me="

    def form_valid(self, form):
        data = form.cleaned_data
        user = User.objects.create_user(data["username"], data["email"], data["password"])
        user.save()
        self.success_url += str(user.id)
        return super().form_valid(form)
    
class LoginFormView(FormView):
    template_name = "main\\login.html"
    form_class = LoginForm
    success_url = "/account/me="

    def form_valid(self, form):
        data = form.cleaned_data
        user = authenticate(username=data["username"], password=data["password"])
        self.success_url += str(user.id)
        return super().form_valid(form)

class MeDetailView(DeleteView):
    model = User
    template_name = "main\\me.html"
    context_object_name = "user"
