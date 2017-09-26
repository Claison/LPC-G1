from django.shortcuts import render

# Create your views here.
from .models import Agenda,Compromisso
from django.http import HttpResponse

#Um usuário pode compartilhar suas agendas com outros usuários;
#Um usuário pode convidar os demais para um compromisso especifico;
#Os usuários convidados podem confirmar ou declinar na participação de um compromisso que foram convidados;

def listaAgenda(request):
    retorno='<h1>Agendas</h1>'
    lista=Agenda.objects.all()
    for a in lista:
        retorno+='</br>Nome das Agendas:{}</br>'.format(a.nome)
    return HttpResponse(retorno)

def get_agenda_ID(request,id):
    retorno='<h1>Agenda</h1>'
    agenda=Agenda.objects.filter(tipo__nome='Publico',usuario__id=id)
    for a in agenda:
        retorno +='</br>Nome da Agenda:{}</br>'.format(a.nome)  
    return HttpResponse(retorno)

def agendaInstitucional(request):
    retorno = "<h1> TODOS OS COMPROMISSOS INSTITUCIONAIS </h1>"
    institucionais = Compromisso.objects.filter(agenda__tipo__nome='Institucional')
    for i in institucionais:
        retorno += '<br> Nome Compromisso: {} <br> <br> '.format(i.nome)
    return HttpResponse(retorno)