from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Todo
from django.urls import reverse_lazy



class TodoListView(ListView):
    model = Todo

class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")