#encoding:utf-8

from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import Context
from django.template import RequestContext
from django.http import HttpResponse
import datetime

def index(request):
    current_date = datetime.datetime.now()
    return render_to_response('index.html', locals())

def index1(request):
    current_date = datetime.datetime.now()
    return render_to_response('index1.html', locals(), context_instance=RequestContext(request))

def hours_ahead(request, offset):
    hour_offset = int(offset)
    next_time = datetime.datetime.now() + datetime.timedelta(hours= hour_offset)
    return render_to_response('hours_ahead.html', locals())

def inters(request):
    current_date = datetime.datetime.now()
    return render_to_response('index.html', locals())


