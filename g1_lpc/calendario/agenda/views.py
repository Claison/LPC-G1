from django.shortcuts import render

# Create your views here.
from .models import Agenda

def agenda(request):
    agendas = Agenda.objects.all()
    retorno = ""
    for agenda in agendas:
        retorno += "<li>"+agenda.nome+"</li>"
    return HttpResponse(retorno)
def listaAgenda(request):
    retorno='<h1>Agendas</h1>'
    lista=Agenda.objects.all()
    for evento in lista:
        retorno+='</br>Nome das Agendas:{}</br>'.format(agenda.nome)
    return HttpResponse(retorno)

def get_agenda_ID(request,id):
    retorno='<h1>Agendas</h1>'
    agenda=Agenda.objects.get(pk=id)
    retorno +='</br>Nome do Evento:{}</br>'.format(agenda.nome)  
    return HttpResponse(retorno)