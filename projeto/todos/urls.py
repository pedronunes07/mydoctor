from django.urls import path
from .views import HomeView, login_view, register_view

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
] 