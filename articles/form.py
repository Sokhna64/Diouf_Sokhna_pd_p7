from django import forms
from .models import Article
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class Editform(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('titre', 'resume', 'contenu', 'miniature')
        widgets = {
            'contenu': SummernoteWidget(),
        }
