import os,sys, json, urllib, urllib2
from os.path import join

from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

def home(request):
    return render_to_response('f1mapp.html');
def info(request):
    return render_to_response('info.html');
def error(request):
    return render_to_response('error.html');
def test(request):
    return render_to_response('test.html');
def mapeditor(request):
    return render_to_response('f1map_editor.html');
def data(request):
    import urllib2
    data = urllib2.urlopen('http://qa.lusob.com/cars_data.json').read()
    return render_to_response('data.html', {"data":data});
