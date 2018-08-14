## -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.
from django.template import RequestContext
from django.http import HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string



@csrf_exempt
def index(request):
    if request.method == "GET":
        return render_to_response("polls.html")
    else:
        trans = request.POST.get('tr_code')
        count = 0
        from urllib3 import HTTPConnectionPool
        from googletrans import Translator
        pool = HTTPConnectionPool('cobold.xyz' , maxsize = 1)
        r = pool.request('GET', '/test/Vodafone_Dump_07-Aug-18.xml',fields = {})
        xml_data = r.data 
	import xml.etree.ElementTree as ET
	root = ET.fromstring(xml_data)
        for i in root.findall('Tariff'):
   	    text = (i.find('Plan_Desc').text)
            r = i.find('Plan_Desc')
            translator = Translator()
            converted_text = translator.translate(text, dest=str(trans))
            converted = converted_text.extra_data["translation"][0][1]
            r.set('updated', converted)
 



