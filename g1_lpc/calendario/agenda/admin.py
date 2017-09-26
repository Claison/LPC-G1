from django.contrib import admin

# Register your models here.
from agenda.models import Agenda,Compromisso


admin.site.register(Agenda)
admin.site.register(Compromisso)