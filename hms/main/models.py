#encoding:utf-8
from django.db import models

# Create your models here.
class ContactType(models.Model):
    name = models.CharField(max_length=50) 

    def __unicode__(self):
        return self.name

class Contact(models.Model):
    contact_type = models.ForeignKey(ContactType, blank=True, null=True)
    description = models.CharField('Descripcion', max_length=60, blank=True, null=True)
    email = models.EmailField('E-Mail',blank=True, null=True)
    first_name = models.CharField('Nombres', max_length=30)
    home_phones = models.CharField('Telefono Casa', max_length=80, blank=True, null=True)
    last_name = models.CharField('Apellidos', max_length=60, blank=True, null=True)    
    office_phones = models.CharField('Telefono Oficina', max_length=80,blank=True, null=True)
    personal_phones = models.CharField('Telefono Personal', max_length=80,blank=True, null=True)
    specialty = models.CharField('Especialidad', max_length=100, blank=True, null=True)
    #image = models.ImageField(upload_to='Contacts', verbose_name='Imagen', blank=True, null=True)
    
    def __unicode__(self):
        return u'%s %s'% (self.first_name, self.last_name)

class Cuarto(models.Model):
    name = models.CharField('Nombre',max_length=50) 

    def __unicode__(self):
        return self.name

class Paciente(models.Model):
    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    nombres =  models.CharField('Nombres', max_length=60, blank=True, null=True)
    apellido_paterno = models.CharField('Apellido Paterno', max_length=60, blank=True, null=True)
    apellido_materno = models.CharField('Apellido Materno', max_length=60, blank=True, null=True)
    edad = models.CharField('Edad', max_length=5, blank=True, null=True)
    sexo = models.CharField('Sexo',max_length=2,choices=SEXO)
    
    
    def __unicode__(self):
        return u'%s %s %s'% (self.apellido_paterno, self.apellido_materno, self.nombres, )
 
class Internamiento(models.Model):
    folio = models.CharField('folio', max_length=7, blank=True, null=True)
   # patient = models.CharField('Paciente', max_length=50, blank=True, null=True)
    paciente = models.ForeignKey(Paciente, blank=True, null=True)
    Cuarto = models.ForeignKey(Cuarto, blank=True, null=True)
    dateTime = models.DateTimeField('Fecha Ingreso',blank=True, null=True)
    medico = models.CharField('Medico Tratante', max_length=40, blank=True, null=True)
    medicoResidente = models.CharField('Medico Recidente', max_length=40, blank=True, null=True)
    disease = models.CharField('Diagnostico', max_length=40, blank=True, null=True)
    patientType = models.CharField('Tipo de Pacinte', max_length=20, blank=True, null=True)
    institution = models.CharField('Institucion', max_length=40, blank=True, null=True)
    Depositos = models.CharField('Depositos', max_length=70, blank=True, null=True)
    Documentos = models.CharField('Documentos', max_length=70, blank=True, null=True)
    fecha_egreso = models.DateTimeField('Fecha Egreso',blank=True, null=True)
   
    def __unicode__(self):
        return self.folio











