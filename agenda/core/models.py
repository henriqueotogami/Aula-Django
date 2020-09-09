from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_Evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_Evento.strftime('%d/%m/%y às %H:%M')

    def get_data_input_evento(self):
        return self.data_Evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_Evento < datetime.now():
            return True
        else:
            return False