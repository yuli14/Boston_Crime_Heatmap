# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class District(models.Model):
    did = models.CharField(primary_key=True, max_length=5)
    geoinfo = models.CharField(max_length=40, blank=True, null=True)
    pid = models.ForeignKey('PoliceStation', models.DO_NOTHING, db_column='pid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'district'


class OffenseCode(models.Model):
    code = models.BigIntegerField(primary_key=True)
    code_description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offense_code'


class Incident(models.Model):
    incident_num = models.CharField(primary_key=True, max_length=10)
    offense_description = models.CharField(max_length=100, blank=True, null=True)
    shooting = models.CharField(max_length=40, blank=True, null=True)
    offense_code_group = models.CharField(max_length=40, blank=True, null=True)
    offense_code = models.ForeignKey('OffenseCode', models.DO_NOTHING, db_column='offense_code')
    did = models.ForeignKey(District, models.DO_NOTHING, db_column='did', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incident'
        unique_together = (('incident_num', 'offense_code'),)


class IncidentLocation(models.Model):
    incident_num = models.ForeignKey(Incident, models.DO_NOTHING, db_column='incident_num', primary_key=True, related_name='IL_incident_num')
    offense_code = models.ForeignKey(Incident, models.DO_NOTHING, db_column='offense_code', related_name='IL_offense_code')
    street = models.CharField(max_length=40, blank=True, null=True)
    reporting_area = models.CharField(max_length=5, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=7, blank=True, null=True)
    longtitude = models.DecimalField(max_digits=9, decimal_places=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incident_location'
        unique_together = (('incident_num', 'offense_code'),)


class IncidentTime(models.Model):
    incident_num = models.ForeignKey(Incident, models.DO_NOTHING, db_column='incident_num', primary_key=True, related_name='IT_incident_num')
    offense_code = models.ForeignKey(Incident, models.DO_NOTHING, db_column='offense_code', related_name='IT_offense_code')
    datetime = models.DateTimeField(blank=True, null=True)
    dayofweek = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incident_time'
        unique_together = (('incident_num', 'offense_code'),)




class PoliceStation(models.Model):
    pid = models.BigIntegerField(primary_key=True)
    ps_name = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'police_station'


class PsLocation(models.Model):
    pid = models.ForeignKey(PoliceStation, models.DO_NOTHING, db_column='pid', primary_key=True)
    street = models.CharField(max_length=40, blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    zipcode = models.CharField(max_length=5, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=7, blank=True, null=True)
    longtitude = models.DecimalField(max_digits=9, decimal_places=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ps_location'
