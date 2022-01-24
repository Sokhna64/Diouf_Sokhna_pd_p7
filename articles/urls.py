from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, about, listarticles, createArticle, contentArticle, editArticle

urlpatterns = [
    path("", home, name='index'),
    path("about/", about, name='about'),
    path("articles/", listarticles, name='listarticles'),
    path("articles/new", createArticle, name="new"),
    path('articles/<int:id>/', contentArticle, name='content'),
    path('pages/<int:id>/', contentArticle, name='content'),
    path('articles/edit/<int:id>/', editArticle, name='edit')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
