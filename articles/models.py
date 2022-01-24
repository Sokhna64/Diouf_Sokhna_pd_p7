
from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    titre = models.CharField(max_length=150)
    resume = models.TextField(blank=True)
    miniature = models.ImageField(blank=True, upload_to="images")
    contenu = models.TextField(blank=True)
    auteur = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titre}"


class Description(models.Model):
    titre = models.CharField(max_length=150)
    contenu = models.TextField(blank=True)

    def __str__(self):
        return f"{self.titre}"
