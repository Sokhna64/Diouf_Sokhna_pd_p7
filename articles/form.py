from django import forms
from .models import Article


class Editform(forms.ModelForm):
    titre = forms.CharField(label="Titre", widget=forms.TextInput(
        attrs={"class": "form-control"}))
    resume = forms.CharField(label="Résumé", widget=forms.Textarea(
        attrs={"class": "form-control"}))
    contenu = forms.CharField(
        label="Contenu", widget=forms.Textarea(attrs={"class": "form-control"}))

    class Meta:
        model = Article
        fields = ('titre', 'resume', 'contenu',
                  'user', 'miniature')
