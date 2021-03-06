# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'ContactType'
        db.create_table('main_contacttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('main', ['ContactType'])

        # Adding model 'Contact'
        db.create_table('main_contact', (
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('contact_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.ContactType'], null=True, blank=True)),
            ('office_phones', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('personal_phones', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
            ('home_phones', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
            ('specialty', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal('main', ['Contact'])

        # Adding model 'Cuarto'
        db.create_table('main_cuarto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('main', ['Cuarto'])

        # Adding model 'Paciente'
        db.create_table('main_paciente', (
            ('edad', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('apellido_paterno', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('apellido_materno', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('nombres', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('main', ['Paciente'])

        # Adding model 'Internamiento'
        db.create_table('main_internamiento', (
            ('patientType', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('folio', self.gf('django.db.models.fields.CharField')(max_length=7, null=True, blank=True)),
            ('medico', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('paciente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Paciente'], null=True, blank=True)),
            ('institution', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('disease', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('dateTime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('Cuarto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Cuarto'], null=True, blank=True)),
            ('Depositos', self.gf('django.db.models.fields.CharField')(max_length=70, null=True, blank=True)),
            ('Documentos', self.gf('django.db.models.fields.CharField')(max_length=70, null=True, blank=True)),
            ('fecha_egreso', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('medicoResidente', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
        ))
        db.send_create_signal('main', ['Internamiento'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'ContactType'
        db.delete_table('main_contacttype')

        # Deleting model 'Contact'
        db.delete_table('main_contact')

        # Deleting model 'Cuarto'
        db.delete_table('main_cuarto')

        # Deleting model 'Paciente'
        db.delete_table('main_paciente')

        # Deleting model 'Internamiento'
        db.delete_table('main_internamiento')
    
    
    models = {
        'main.contact': {
            'Meta': {'object_name': 'Contact'},
            'contact_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.ContactType']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'home_phones': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'office_phones': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'personal_phones': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'specialty': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'main.contacttype': {
            'Meta': {'object_name': 'ContactType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'main.cuarto': {
            'Meta': {'object_name': 'Cuarto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'main.internamiento': {
            'Cuarto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Cuarto']", 'null': 'True', 'blank': 'True'}),
            'Depositos': ('django.db.models.fields.CharField', [], {'max_length': '70', 'null': 'True', 'blank': 'True'}),
            'Documentos': ('django.db.models.fields.CharField', [], {'max_length': '70', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Internamiento'},
            'dateTime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'disease': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'fecha_egreso': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'folio': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'medico': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'medicoResidente': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'paciente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Paciente']", 'null': 'True', 'blank': 'True'}),
            'patientType': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        'main.paciente': {
            'Meta': {'object_name': 'Paciente'},
            'apellido_materno': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'apellido_paterno': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'edad': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombres': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }
    
    complete_apps = ['main']
