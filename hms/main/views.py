from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from hms.main.models import Paciente, Contact, Internamiento
from hms.main.forms import ContactForm
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from django.template import RequestContext
from datetime import datetime
from django.utils.formats import get_format

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

import sys
import xlrd
import MySQLdb
from django.utils.encoding import smart_str, smart_unicode
from django.db.models import Q

from django.core import serializers


from django.utils import simplejson

def vote(request):
    results = {'success':False}
    if request.method == u'GET':
      GET = request.GET
      if GET.has_key(u'pk') and GET.has_key('vote'):
        pk = int(GET[u'pk'])
        vote = GET[u'vote']

        if vote == u'up':
          aglo='dfdsf'
        elif vote == u'down':
          algomas='dfdsfdsdfg'
        results = {'success':True}
    json = simplejson.dumps(results)
    return HttpResponse(json, mimetype='application/json')

def nuevo_usuario(request):
    if request.method == 'POST':
       formulario = UserCreationForm(request.POST)
       if formulario.is_valid:
          formulario.save()
          return HttpResponseRedirect('/')
    else:
         formulario = UserCreationForm()
    return render_to_response('nuevousuario.html',{'formulario':formulario},context_instance=RequestContext(request))


def nuevo_contacto(request):
    if request.method == 'POST':
       formulario = ContactForm(request.POST)
       if formulario.is_valid():
          formulario.save()
          return HttpResponseRedirect('/admin/main/contact/')
    else:
        formulario = ContactForm()
    return render_to_response('contactoform.html',{'formulario':formulario},context_instance=RequestContext(request))

def contacto(request):
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            titulo = 'Mensaje desde HMS'
            contenido = formulario.cleaned_data['mensaje']+"\n"
            contenido += 'Comunicarse a: '+ formulario.cleaned_data['correo']
            correo = EmailMessage(titulo, contenido, to=['sistemashms@gmail.com'])
            correo.send()
            return HttpResponseRedirect('/')
    else:
        formulario = ContactForm()
    return render_to_response('contactoform.html',{'formulario':formulario}, context_instance=RequestContext(request))
    

def index(request):
    return render_to_response('index1.html',context_instance=RequestContext(request))

def servicios(request):
    return render_to_response('servicios.html',context_instance=RequestContext(request))

def ubicacion(request):
    return render_to_response('ubicacion.html',context_instance=RequestContext(request))

def derechosPacientesAleman(request):
    return render_to_response('derechosPacientesAleman.html',context_instance=RequestContext(request))

def derechosPacientes(request):
    return render_to_response('derechosPacientes.html',context_instance=RequestContext(request))

def derechosMedicos(request):
    return render_to_response('derechosMedicos.html',context_instance=RequestContext(request))

def derechosEnfermeras(request):
    return render_to_response('derechosEnfermeras.html',context_instance=RequestContext(request))

def informes(request):
    return render_to_response('informesHMS.html',context_instance=RequestContext(request))

def directorioMedico(request):
    especialidades = Contact.objects.filter(contact_type__name = "MEDICO").values('specialty').distinct().order_by('specialty')
    return render_to_response('directorioMedico.html',{'especialidades':especialidades},context_instance=RequestContext(request))

def internamientos(request):
    internamientos = Internamiento.objects.order_by('Cuarto').filter(
        Q(fecha_egreso__gt=datetime.now()) | Q(fecha_egreso__isnull=True)
    )

    today = datetime.now() #fecha actual
    f2 = today
    intenamientosData = []
    for internamiento in internamientos:
        f1 = datetime(internamiento.dateTime.year, internamiento.dateTime.month, internamiento.dateTime.day)
        diasEstancia = (datetime.now()- internamiento.dateTime).days
        intenamientosData.append ({'folio': internamiento.folio,
         'paciante': "%s %s %s" % (internamiento.paciente.apellido_paterno, internamiento.paciente.apellido_materno , internamiento.paciente.nombres),
         'Cuarto': internamiento.Cuarto,
         'dateTime': internamiento.dateTime,
         'medico': internamiento.medico,
         'disease': internamiento.disease,
         'patientType': internamiento.patientType,
         'institution': internamiento.institution,
         'diasEstancia': str(f2.toordinal() - f1.toordinal()),                  
                 })
        
    return render_to_response('internamientos.html', {'fecha_actual':today,
                                                      'intenamientosData':intenamientosData,
                                                      })

def subirDatos(request):
    doc = xlrd.open_workbook('/home/chunel/MEDICOS.xls')
    sheet = doc.sheet_by_index(0)

    nrows = sheet.nrows
    sim = []



    db = MySQLdb.connect(user='hmsuser', db='hms_db', passwd='hms', host='localhost') 
    cursor = db.cursor()
    print(nrows)

    for i in range(nrows):
        valores = []
        insert_query = ""
        print("%s algo "% insert_query)
        valores.append(2)                          # contact_type_id
        valores.append("")                         # description
        valores.append("")                         # email
        valores.append(smart_str(sheet.cell_value(i,0)).replace("'","")) # first_name
        valores.append(smart_str(sheet.cell_value(i,5)).replace("'","")) # home_phones
        valores.append(ord(sheet.cell_value(i,1))) # last_name
        print(sheet.cell_value(i,1))
        valores.append(smart_str(sheet.cell_value(i,4)).replace("'","")) # office_phones
        valores.append(smart_str(sheet.cell_value(i,3)).replace("'","")) # personal_phones
        valores.append(smart_str(sheet.cell_value(i,2)).replace("'","")) # specialty
        insert_query = 'insert into main_contact(contact_type_id, description, email, first_name, home_phones, last_name, office_phones, personal_phones, specialty) values %s;'% str(tuple(valores))
        print(insert_query)
        #try:
        # Execute the SQL command
        #cursor.execute(insert_query)
        # Commit your changes in the database
        #db.commit()
        #except:
        # Rollback in case there is any error
        #print("ERROR")
        #db.rollback()

    # disconnect from server
    db.close()
    return HttpResponse(insert_query)

def search(request, query):
  
  query = request.GET['query']
  contacts = 1
  if query != "":
    contacts = Contact.objects.filter(contact_type__name__icontains='MEDICO').filter(
                                                                                  Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(specialty__icontains=query) 
                                                                                  )
  context = {'doctores':contacts,'query': query}
  return render_to_response('directorioMedico.html', context, context_instance=RequestContext(request))

