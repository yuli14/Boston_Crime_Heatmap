# Generated by Django 2.0.5 on 2018-11-29 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=80, null=True, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('codename', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.CharField(blank=True, max_length=254, null=True)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('did', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('geoinfo', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'district',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(blank=True, max_length=200, null=True)),
                ('action_flag', models.IntegerField()),
                ('change_message', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(blank=True, max_length=100, null=True)),
                ('model', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField(blank=True, null=True)),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('incident_num', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('offense_description', models.CharField(blank=True, max_length=100, null=True)),
                ('shooting', models.CharField(blank=True, max_length=40, null=True)),
                ('offense_code_group', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'incident',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OffenseCode',
            fields=[
                ('code', models.BigIntegerField(primary_key=True, serialize=False)),
                ('code_description', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'offense_code',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PoliceStation',
            fields=[
                ('pid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('ps_name', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'police_station',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IncidentLocation',
            fields=[
                ('incident_num', models.ForeignKey(db_column='incident_num', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='location_incident_number', serialize=False, to='BC.Incident')),
                ('street', models.CharField(blank=True, max_length=40, null=True)),
                ('reporting_area', models.CharField(blank=True, max_length=5, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=7, max_digits=9, null=True)),
                ('longtitude', models.DecimalField(blank=True, decimal_places=7, max_digits=9, null=True)),
                ('district', models.CharField(blank=True, max_length=5, null=True)),
            ],
            options={
                'db_table': 'incident_location',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IncidentTime',
            fields=[
                ('incident_num', models.ForeignKey(db_column='incident_num', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='time_incident_number', serialize=False, to='BC.Incident')),
                ('datetime', models.DateTimeField(blank=True, null=True)),
                ('dayofweek', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'incident_time',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PsLocation',
            fields=[
                ('pid', models.ForeignKey(db_column='pid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='BC.PoliceStation')),
                ('street', models.CharField(blank=True, max_length=40, null=True)),
                ('city', models.CharField(blank=True, max_length=40, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=5, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=7, max_digits=9, null=True)),
                ('longtitude', models.DecimalField(blank=True, decimal_places=7, max_digits=9, null=True)),
            ],
            options={
                'db_table': 'ps_location',
                'managed': False,
            },
        ),
    ]
