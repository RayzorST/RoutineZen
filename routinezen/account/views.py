from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.views.generic import DeleteView
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from .forms import RegistrationFrom, LoginForm

def account(request):
    if request.user.is_authenticated:
        return redirect(f"/account/me={request.user.id}")
    return redirect("/account/login")

class RegistrationFormView(FormView):
    template_name = "main\\registration.html"
    form_class = RegistrationFrom
    success_url = "/account/me="

    def form_valid(self, form):
        ### НЕТ ПРОВЕРОК
        data = form.cleaned_data
        user = User.objects.create_user(data["username"], data["email"], data["password"])
        user.save()
        login(self.request, user)
        self.success_url += str(user.id)
        return super().form_valid(form)
    
class LoginFormView(FormView):
    template_name = "main\\login.html"
    form_class = LoginForm
    success_url = "/account/me="

    def form_valid(self, form):
        ### НЕТ ПРОВЕРОК
        self.request.user.is_authenticated
        data = form.cleaned_data
        user = authenticate(username=data["username"], password=data["password"])
        login(self.request, user)
        self.success_url += str(user.id)
        self.request.session["userid"] = user.id
        return super().form_valid(form)

class MeDetailView(DeleteView):
    model = User
    template_name = "main\\me.html"
    context_object_name = "user"
