from django.urls import path
from .views import HomeView, login_view, register_view, dashboard_view, agendar_consulta_view, ver_consultas_view

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('agendar-consulta/', agendar_consulta_view, name='agendar_consulta'),
    path('ver-consultas/', ver_consultas_view, name='ver_consultas'),
] 