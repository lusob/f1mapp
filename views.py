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