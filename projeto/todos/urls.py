from django.urls import path
from .views import HomeView, login_view, register_view, dashboard_view, agendar_consulta_view

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('agendar-consulta/', agendar_consulta_view, name='agendar_consulta'),
] 