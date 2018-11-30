from django.shortcuts import render_to_response,render
from django.template.response import TemplateResponse
from django.template import Context, loader
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from BC.models import Incident,IncidentLocation,PsLocation
from decimal import Decimal
from django.db import connection
import json


# def index(request):
#     incident_list = Incident.objects.filter(offense_code=111)
#     # incident_list = IncidentLocation.objects.all()[0:9].values_list('latitude','longtitude')
#
#     tmpl = loader.get_template("index.html")
#     cont = Context({'Incident': incident_list})
#     return HttpResponse(tmpl.render(cont.flatten()))

def map(request):
    # longtitude_list = IncidentLocation.longtitude
    # latlong_list = IncidentLocation.objects.all()[0:9].values_list('latitude','longtitude')
    latlong_list = IncidentLocation.objects.all()
    police_list = PsLocation.objects.all()

    # police_list = PsLocation.objects.all()[0:9].values_list('latitude','longtitude')
    # latlong_list_json = json.dumps(list(latlong_list),cls=DjangoJSONEncoder)
    # latlong_list =serializers.serialize("json",IncidentLocation.objects.all())
    tmpl = loader.get_template("map.html")
    print(type(latlong_list))
    cont1 = {'location': latlong_list,'ps_location':police_list}
    print(type(police_list))


    # cont = Context({'location':latlong_list})
    return HttpResponse(tmpl.render(cont1,request))


    # return HttpResponse(tmpl.render(json.dumps(cont1), content_type="application/json"),request)
    # return HttpResponse('map.html')
    # return render_to_response('map.html')

# def my_sql()
# def team(request):
#     return
# def articlespage(request):
#     return render(request, 'Articles/home.html')
#
#
# def successpage(request):
#     data = request.POST.get('textbox1')
#
#     context = {'data': data}
#     return render(request, 'Articles/successpage.html', context)

# Create your views here.

