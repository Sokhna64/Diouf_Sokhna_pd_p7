import contextlib

from datetime import datetime
import logging
from operator import ne
from django.shortcuts import get_object_or_404, render, redirect
from django.template import context
from .models import Article, Description
from django.contrib.auth.decorators import login_required
from .form import Editform


@login_required(login_url="/login/")
def home(request):
    user = request.user
    desc = Description.objects.all()
    articles = Article.objects.all()[:6]
    return render(request, "pages/index.html", {"desc": desc, "articles": articles})


def about(request):
    desc = Description.objects.all()
    return render(request, "pages/about.html", {"desc": desc})


@login_required(login_url="/login")
def listarticles(request):
    user = request.user
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, "articles/listarticles.html", context)


@login_required(login_url="/login/")
def createArticle(request):
    user = request.user
    if request.method == "POST":
        form = Editform(request.POST, request.FILES)
        if form.is_valid():
            newArticle = form.save(commit=False)
            newArticle.user = user
            newArticle.save()
            return redirect("/articles/")
    else:
        form = Editform()
    context = {"form": form, "user": user}
    return render(request, "articles/new.html", context)


@login_required(login_url="/login/")
def contentArticle(request, id):
    user = request.user
    article = get_object_or_404(Article, id=id)
    context = {"article": article, "user": user}
    return render(request, "articles/content.html", context)


@login_required(login_url="/login/")
def editArticle(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == "POST":
        form = Editform(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("/articles/")
    else:
        form = Editform(instance=article)
    context = {"article": article, "form": form}
    return render(request, "articles/edit.html", context)


@login_required(login_url="/login/")
def deleteArticle(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == "POST":
        article.delete()
        return redirect("/articles/")
    return render(request, "articles/delete.html", {"article": article})
