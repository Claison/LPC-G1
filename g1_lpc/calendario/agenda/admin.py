from django.contrib import admin

# Register your models here.
from agenda.models import AgendaPublica, AgendaPrivada,AgendaInstitucional,Compromisso,Usuario


admin.site.register(AgendaPublica)
admin.site.register(AgendaPrivada)
admin.site.register(AgendaInstitucional)
admin.site.register(Compromisso)
admin.site.register(Usuario)