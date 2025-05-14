from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Todo, Consulta
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here.
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

def voltar_para_index(request):
    return redirect('home')

class TodoListView(ListView):
    model = Todo
    template_name = 'todos/todo_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['voltar_url'] = reverse_lazy('home')
        return context

class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")
    template_name = 'todos/todo_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['voltar_url'] = reverse_lazy('home')
        return context

class HomeView(TemplateView):
    template_name = 'todos/index.html'

def dashboard_view(request):
    context = {'voltar_url': reverse_lazy('home')}
    return render(request, 'todos/dashboard.html', context)

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
        except User.DoesNotExist:
            user = None
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Email ou senha incorretos!')
    context = {'voltar_url': reverse_lazy('home')}
    return render(request, 'todos/login.html', context)

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        full_name = request.POST.get('full_name', '')
        phone = request.POST.get('phone', '')
        birthdate = request.POST.get('birthdate', '')
        if password != password2:
            messages.error(request, 'As senhas não coincidem!')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de usuário já existe!')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já cadastrado!')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = full_name
            user.last_name = f"{phone} / {birthdate}"
            user.save()
            messages.success(request, 'Cadastro realizado com sucesso! Faça login.')
            return redirect('login')
    context = {'voltar_url': reverse_lazy('home')}
    return render(request, 'todos/register.html', context)

@login_required
def ver_consultas_view(request):
    consultas = Consulta.objects.filter(usuario=request.user).order_by('-data', '-hora')
    context = {
        'consultas': consultas,
        'voltar_url': reverse_lazy('home')
    }
    return render(request, 'todos/ver_consultas.html', context)

@login_required
def agendar_consulta_view(request):
    if request.method == 'POST':
        especialidade = request.POST['especialidade']
        data = request.POST['data']
        hora = request.POST['hora']
        observacoes = request.POST.get('obs', '')
        Consulta.objects.create(
            usuario=request.user,
            especialidade=especialidade,
            data=data,
            hora=hora,
            observacoes=observacoes
        )
        return redirect('ver_consultas')
    context = {'voltar_url': reverse_lazy('home')}
    return render(request, 'todos/agendar_consulta.html', context)