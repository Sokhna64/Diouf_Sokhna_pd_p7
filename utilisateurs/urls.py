from django.urls import path
from .views import auth, registration
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', auth, name='auth'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', registration, name='register')
]
