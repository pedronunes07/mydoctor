from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
	title = models.CharField(max_length=100, null=False, blank=False)
	created_at =models.DateField(auto_now_add=True,null=False,blank=False)
	deadline = models.DateField(null=False, blank=False)
	finished_at = models.DateField(null=True)

class Consulta(models.Model):
	usuario = models.ForeignKey(User, on_delete=models.CASCADE)
	especialidade = models.CharField(max_length=50)
	data = models.DateField()
	hora = models.TimeField()
	observacoes = models.TextField(blank=True)
	criada_em = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.especialidade} em {self.data} às {self.hora} ({self.usuario.username})"