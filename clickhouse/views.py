# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse
import urllib2
import requests
import csv
import json

# Create your views here.

CLICKHOUSE_BASE_URL = 'http://localhost:8123/?query=' 

def api(request):
    query = request.GET['query']
    database = request.GET.get('database', None)
    table = request.GET.get('table', None)
    url = CLICKHOUSE_BASE_URL + query
    if database is not None:
        url += '&database=' + database
    data = requests.get(url)	
    if table is None:
        objects = [ [y for y in x.split('\t')] for x in data.text.splitlines()]
    else:
        urld = CLICKHOUSE_BASE_URL + 'describe table ' + table
        describe = requests.get(urld)
        describer = [ [y for y in x.split('\t')] for x in describe.text.splitlines()]
        objects = [ {describer[i][0]:y for i,y in enumerate(x.split('\t'))} for x in data.text.splitlines()]
                
    json_data = json.dumps({'objects': objects})
    return HttpResponse(json_data, content_type='application/json')
