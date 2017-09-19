from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=128)
    email = models.CharField(max_length=258)
    
    def __str__(self):
        return self.nome   

class Agenda(models.Model):
    nome = models.CharField(max_length=128)
    data = models.DateTimeField()
    
class AgendaInstitucional(Agenda):
    
    def __str__(self):
        return self.nome
class AgendaPrivada(Agenda):
    def __str__(self):
        return self.nome
class AgendaPublica(Agenda):
    def __str__(self):
        return self.nome
class Compromisso(models.Model):
    nome = models.CharField(max_length=128)
    data_inicio = models.DateTimeField()
    data_Fim = models.DateTimeField()
    local = models.CharField(max_length=128)
    usuario = models.ForeignKey(Usuario, related_name='usuario', null=True, blank=False)
    agenda = models.ForeignKey(Agenda, related_name='agenda', null=True, blank=False)
    def __str__(self):
        return self.nome 