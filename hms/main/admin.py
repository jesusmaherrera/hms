from django.contrib import admin
from hms.main.models import Contact, ContactType, Cuarto, Internamiento, Paciente

class ContactAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'contact_type', 'specialty', 'office_phones', 'home_phones', 'personal_phones', 'description', 'email')
    list_display = ('first_name', 'last_name', 'specialty','description','office_phones','home_phones','personal_phones','contact_type')
    search_fields = ('first_name', 'last_name','specialty','description')

class InternamientoAdmin(admin.ModelAdmin):
    fields = ('folio','paciente', 'Cuarto', 'dateTime', 'medico','medicoResidente', 'disease', 'patientType', 'institution','Depositos','Documentos','fecha_egreso',)
    list_display = ('folio','paciente', 'Cuarto', 'dateTime', 'medico', 'medicoResidente', 'disease', 'patientType', 'institution','Depositos','Documentos','fecha_egreso',)
    ordering = ('fecha_egreso','Cuarto',)
    search_fields = ('paciente__nombres','paciente__apellido_paterno','paciente__apellido_materno','medico',)
    
    #list_filter = ('paciente__nombres',)
    
admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactType)
admin.site.register(Cuarto)
admin.site.register(Paciente)
admin.site.register(Internamiento, InternamientoAdmin)

