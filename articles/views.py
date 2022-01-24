import contextlib
from datetime import datetime
import logging
from django.shortcuts import get_object_or_404, render, redirect
from .models import Article, Description
from django.contrib.auth.decorators import login_required


def home(request):
    desc = Description.objects.all()
    articles = Article.objects.all()
    return render(request, "pages/index.html", {"desc": desc, "articles": articles})


def about(request):
    return render(request, "pages/about.html")


@login_required(login_url="/login")
def listarticles(request):
    user = request.user
    print("user", user)
    articles = Article.objects.filter(user=user)
    return render(request, "articles/listarticles.html", {"articles": articles})


@login_required(login_url="/login/")
def createArticle(request):
    if request.method == "POST":
        user = request.user
        auteur = request.POST['auteur']
        titre = request.POST['titre']
        resume = request.POST['resume']
        contenu = request.POST['contenu']
        miniature = request.FILES['image']
        article = Article.objects.create(
            user=user, auteur=auteur, titre=titre, resume=resume, contenu=contenu, miniature=miniature)
        article.save()
        return redirect("/articles/")

    return render(request, "articles/new.html")


@login_required(login_url="/login/")
def contentArticle(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, "articles/content.html", {"article": article})


def editArticle(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == "POST":

        auteur = request.POST['auteur']
        titre = request.POST['titre']
        resume = request.POST['resume']
        contenu = request.POST['contenu']
        miniature = request.FILES['image']
        Article.objects.filter(pk=article.id).update(
            auteur=auteur, titre=titre, resume=resume, contenu=contenu, miniature=miniature)
        return redirect("/articles/")

    return render(request, "articles/edit.html", {"article": article})
