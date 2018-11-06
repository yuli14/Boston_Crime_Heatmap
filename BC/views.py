


from django.template import Context, loader
from django.http import HttpResponse
from BC.models import Incident


def index(request):
    incident_list = Incident.objects.filter(offense_code=111)
    tmpl = loader.get_template("index.html")
    cont = Context({'Incident': incident_list})
    return HttpResponse(tmpl.render(cont.flatten()))





# Create your views here.

