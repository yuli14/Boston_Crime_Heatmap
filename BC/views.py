from django.shortcuts import render_to_response,render
from django.template.response import TemplateResponse
from django.template import Context, loader
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from BC.models import Incident,IncidentLocation,PsLocation,IncidentTime
from .forms import IForm, ILocationForm, ITimeForm
from decimal import Decimal
from django.db import connection
from django.shortcuts import redirect
import json


def index(request):
    incident_list = IncidentTime.objects.filter(offense_code=111)

    for x in incident_list:
         print(str(x.datetime))
    # incident_list = IncidentLocation.objects.all()[0:9].values_list('latitude','longtitude')

    tmpl = loader.get_template("index.html")
    cont = Context({'Incident': incident_list})
    return HttpResponse(tmpl.render(cont.flatten()))

"""
def map(request):
    # longtitude_list = IncidentLocation.longtitude
    # latlong_list = IncidentLocation.objects.all()[0:9].values_list('latitude','longtitude')
    latlong_list = IncidentLocation.objects.values('latitude','longtitude','district')
    police_list = PsLocation.objects.all()
    IncidentTime_list = IncidentTime.objects.values('datetime','dayofweek','offense_code')

    # police_list = PsLocation.objects.all()[0:9].values_list('latitude','longtitude')
    # latlong_list_json = json.dumps(list(latlong_list),cls=DjangoJSONEncoder)
    # latlong_list =serializers.serialize("json",IncidentLocation.objects.all())
    tmpl = loader.get_template("map.html")
    print(type(latlong_list))
    cont1 = {'location': latlong_list,'ps_location':police_list,'IncidentTime':IncidentTime_list}
    print(type(police_list))


    # cont = Context({'location':latlong_list})
    return HttpResponse(tmpl.render(cont1,request))
"""

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


def new_incident(request):

    if request.method == "POST":
        iform = IForm(request.POST)
        if iform.is_valid():
            post = iform.save(commit=False)
            # post.author = request.user

            incident_num = iform.cleaned_data["incident_num"]

            request.session['incident_num'] = incident_num

            offense_code = iform.cleaned_data["offense_code"].code

            request.session['offense_code'] = offense_code


            post.save()
            return redirect('new_itime')
    else:
        iform = IForm()


    return render(request, 'new_incident.html', {'iform': iform})



def new_itime(request):

    incident_num2 = request.session.get('incident_num')
    offense_code2 = request.session.get('offense_code')

    if request.method == "POST":
        itform = ITimeForm(request.POST)

        if itform.is_valid():
            post1 = itform.save(commit=False)
            datetime = post1.datetime
            print("************************")
            print("validddd")
            print(datetime)
            x=Incident.objects.get(incident_num=incident_num2, offense_code=offense_code2)

            post1.offense_code = x.offense_code
            post1.incident_num = x
            post1.offense_code.clean()


            post1.save()
        else:
            print("not validddd")
        return redirect('new_ilocation')


    else:
        itform = ITimeForm()

    return render(request, 'new_itime.html', {'itform': itform})


def new_ilocation(request):

    incident_num3 = request.session.get('incident_num')
    offense_code3 = request.session.get('offense_code')

    if request.method == "POST":
        ilform = ILocationForm(request.POST)

        if ilform.is_valid():
            post2 = ilform.save(commit=False)

            x=Incident.objects.get(incident_num=incident_num3, offense_code=offense_code3)
            post2.offense_code = x.offense_code
            post2.incident_num = x
            post2.offense_code.clean()

            y = post2.offense_code



            post2.save()

        return redirect('index')
    else:
        ilform = ILocationForm()

    return render(request, 'new_ilocation.html', {'ilform': ilform})


def map(request):

    latlong_list = IncidentLocation.objects.values('latitude', 'longtitude', 'district')
    police_list = PsLocation.objects.all()
    IncidentTime_list = IncidentTime.objects.values('datetime', 'dayofweek', 'offense_code')


    tmpl = loader.get_template("map.html")
    print(type(latlong_list))
    cont1 = {'location': latlong_list, 'ps_location': police_list, 'IncidentTime': IncidentTime_list}
    print(type(police_list))

    # cont = Context({'location':latlong_list})
    return HttpResponse(tmpl.render(cont1, request))