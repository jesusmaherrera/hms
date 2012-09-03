# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
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

        # Adding field 'Internamiento.paciente'
        db.add_column('main_internamiento', 'paciente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Paciente'], null=True, blank=True), keep_default=False)
    
    
    def backwards(self, orm):
        
        # Deleting model 'Paciente'
        db.delete_table('main_paciente')

        # Deleting field 'Internamiento.paciente'
        db.delete_column('main_internamiento', 'paciente_id')
    
    
    models = {
        'main.contact': {
            'Meta': {'object_name': 'Contact'},
            'contact_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.ContactType']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'home_phones': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'fechaEgero': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'folio': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'medico': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'paciente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Paciente']", 'null': 'True', 'blank': 'True'}),
            'patient': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
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
