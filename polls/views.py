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
import requests


@csrf_exempt
def index(request):
    if request.method == "GET":
        return render_to_response("polls.html")
    else:
        print "inside post"
        trans = request.POST.get('tr_code')
        from urllib3 import HTTPConnectionPool
        from googletrans import Translator
        #pool = HTTPConnectionPool('cobold.xyz' , maxsize = 1)
        #r = pool.request('GET', '/test/Vodafone_Dump_07-Aug-18.xml',fields = {})
        #xml_data = r.data
        r = requests.get(url = "http://cobold.xyz/test/Vodafone_Dump_07-Aug-18.xml")
	xml_data = r._content
        print "data received"
	import xml.etree.ElementTree as ET
	root = ET.fromstring(xml_data)
        for i in root.findall('Tariff'):
   	    #i.find('Plan_Desc').text = "MOHIT"
            translator = Translator()
            converted_text = translator.translate(text, dest=str(trans))
            converted = converted_text.extra_data["translation"][0][1]
   	    i.find('Plan_Desc').text = converted
        print root
    return HttpResponse("I AM FINISHED") 



