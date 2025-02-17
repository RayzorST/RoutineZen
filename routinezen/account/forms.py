from django import forms

class RegistrationFrom(forms.Form):
    username = forms.CharField()
    email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

    fields = ('username', 'email', 'password')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    fields = ('username', 'password')