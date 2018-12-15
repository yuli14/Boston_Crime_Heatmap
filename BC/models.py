# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)


    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class District(models.Model):
    did = models.CharField(primary_key=True, max_length=5)
    geoinfo = models.CharField(max_length=40, blank=True, null=True)
    pid = models.ForeignKey('PoliceStation', models.DO_NOTHING, db_column='pid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'district'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class OffenseCode(models.Model):
    code = models.BigIntegerField(primary_key=True)
    code_description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.code)

    class Meta:
        managed = False
        db_table = 'offense_code'



class Incident(models.Model):
    incident_num = models.CharField(primary_key=True, max_length=10)
    offense_description = models.CharField(max_length=100, blank=True, null=True)
    shooting = models.CharField(max_length=40, blank=True, null=True)
    offense_code_group = models.CharField(max_length=40, blank=True, null=True)
    offense_code = models.ForeignKey('OffenseCode', models.DO_NOTHING, db_column='offense_code')

    def __str__(self):
        return self.incident_num

    class Meta:
        managed = False
        db_table = 'incident'
        unique_together = (('incident_num', 'offense_code'),)


class IncidentLocation(models.Model):
    incident_num = models.ForeignKey(Incident, models.DO_NOTHING, db_column='incident_num', primary_key=True,related_name='location_incident_number')
    offense_code = models.ForeignKey(OffenseCode, models.DO_NOTHING, db_column='offense_code',related_name='location_offense_code')
    street = models.CharField(max_length=40, blank=True, null=True)
    reporting_area = models.CharField(max_length=5, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=7, blank=True, null=True)
    longtitude = models.DecimalField(max_digits=9, decimal_places=7, blank=True, null=True)
    district = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incident_location'
        unique_together = (('incident_num', 'offense_code'),)


class IncidentTime(models.Model):
    incident_num = models.ForeignKey(Incident, models.DO_NOTHING, db_column='incident_num', primary_key=True,related_name='time_incident_number')
    offense_code = models.ForeignKey(OffenseCode, models.DO_NOTHING, db_column='offense_code',related_name='time_offense_code')
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
