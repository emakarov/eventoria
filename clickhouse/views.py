# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse
import urllib2
import requests
import csv
import json
from django.template import Template, RequestContext, loader, Context


CLICKHOUSE_BASE_URL = 'http://localhost:8123/?query=' 
CLICKHOUSE_DASHBOARD_TEMPLATE = 'clickhouse/dashboard.html'

def api(request):
    query = request.GET['query']
    database = request.GET.get('database', None)
    table = request.GET.get('table', None)
    query += " format JSON"
    url = CLICKHOUSE_BASE_URL + query
    if database is not None:
        url += '&database=' + database
    data = requests.get(url)	
    json_data = data.text
    return HttpResponse(json_data, content_type='application/json')


def dashboard(request):
    return render(request, CLICKHOUSE_DASHBOARD_TEMPLATE, {})
