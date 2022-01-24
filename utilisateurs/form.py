from django import forms
# class django pour creer un utilisateur, la class registration va heriter de cette classe
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", widget=forms.TextInput(
        attrs={"class": "form-control"}))
    password = forms.CharField(
        label="Mot de passe", widget=forms.PasswordInput(attrs={"class": "form-control"}))

# ici on a utilisé l'autre modele pour faire un formulaire: model form (on a utilisé forms pour la classe precedente)


class RegisterForm(UserCreationForm):
    username = forms.CharField(label="Nom d'utilisateur", widget=forms.TextInput(
        attrs={"class": "form-control"}))
    email = forms.CharField(label="Email", widget=forms.EmailInput(
        attrs={"class": "form-control"}))
    password1 = forms.CharField(
        label="Mot de passe", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(
        label="Confirmation", widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
