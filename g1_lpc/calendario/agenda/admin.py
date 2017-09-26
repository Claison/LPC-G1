from django.contrib import admin

# Register your models here.
from agenda.models import Agenda,Compromisso,UsuarioAgenda,UsuarioCompromisso


admin.site.register(Agenda)
admin.site.register(Compromisso)
admin.site.register(UsuarioAgenda)
admin.site.register(UsuarioCompromisso)