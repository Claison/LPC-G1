from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Um usuário pode compartilhar suas agendas com outros usuários;
#Um usuário pode convidar os demais para um compromisso especifico;
#Os usuários convidados podem confirmar ou declinar na participação de um compromisso que foram convidados;

class Tipo(models.Model):
    nome = models.CharField(max_length=128)

class Agenda(models.Model):
    nome = models.CharField(max_length=128)
    data = models.DateTimeField()
    tipo=models.ForeignKey(Tipo)
    def __str__(self):
        return self.nome

class UsuarioAgenda(models.Model):
    usuario = models.ForeignKey(User)
    agenda = models.ForeignKey(Agenda)

    def __str__(self):
         return "Usuário: {} Agenda: {}".format(self.usuario,self.agenda)


class Compromisso(models.Model):
    nome = models.CharField(max_length=128)
    data_inicio = models.DateTimeField()
    data_Fim = models.DateTimeField()
    local = models.CharField(max_length=128)
    agenda = models.ForeignKey(Agenda, related_name='agenda', null=True, blank=False)
    def __str__(self):
        return self.nome 

class UsuarioCompromisso(models.Model):
     usuario = models.ForeignKey(User)
     compromisso = models.ForeignKey(Compromisso)
     aceite = models.BooleanField(default=True,verbose_name='Você aceita o convite')

     def __str__(self):
         return "Usuário: {} Compromisso: {}".format(self.usuario,self.compromisso)