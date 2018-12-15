from django import forms
from django.forms.widgets import DateInput

from .models import Incident, IncidentLocation, IncidentTime
from django.forms import inlineformset_factory

class IForm(forms.ModelForm):

    class Meta:
        model = Incident
        fields = ('incident_num', 'offense_code', 'offense_description', 'shooting')

class ITimeForm(forms.ModelForm):
    datetime = forms.DateTimeField(required=False, input_formats=['%Y-%m-%d %H:%M:%S'])

    class Meta:
        model = IncidentTime

        fields = ('dayofweek','datetime',)





class ILocationForm(forms.ModelForm):
    class Meta:
        model = IncidentLocation
        #fields = ( 'latitude', 'longtitude', 'district')
        #fields = ('latitude', 'longtitude', 'district')
        exclude = ('incident_num', 'offense_code')




