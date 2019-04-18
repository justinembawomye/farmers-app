# Generated by Django 2.2 on 2019-04-17 14:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='kampala', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='planting-season', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='SubCounty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='kagoma', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('area', models.CharField(max_length=100)),
                ('rice_type', models.CharField(max_length=50)),
                ('sowing_date', models.DateField(default=datetime.date.today)),
                ('sowing_type', models.CharField(max_length=50)),
                ('Planting_type', models.CharField(max_length=50)),
                ('Levelling', models.CharField(max_length=50)),
                ('ridge', models.CharField(max_length=50)),
                ('watercourse_state', models.CharField(max_length=50)),
                ('fertilizers', models.BooleanField(default=True)),
                ('weed_condition', models.CharField(max_length=100)),
                ('harvest_date', models.DateField(default=datetime.date.today)),
                ('total_harvest', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=200)),
                ('photo', models.ImageField(default='default.jpg', upload_to='profile_pictures')),
                ('season', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Season')),
            ],
        ),
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('login_id', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=50)),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.District')),
                ('subcounty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.SubCounty')),
            ],
        ),
        migrations.CreateModel(
            name='Harvest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('area', models.CharField(max_length=100)),
                ('Harvest', models.CharField(max_length=50)),
                ('season', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Season')),
            ],
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=50)),
                ('marriage_status', models.CharField(choices=[('M', 'Married'), ('S', 'Single')], default='single', max_length=30, null=True)),
                ('telephone', models.CharField(max_length=20)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pictures')),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'male')], default='other', max_length=20, null=True)),
                ('village', models.CharField(max_length=100)),
                ('community_status', models.CharField(max_length=100)),
                ('instructor_possibility', models.BooleanField(default=True)),
                ('farm_area', models.CharField(max_length=100)),
                ('crop_type', models.CharField(max_length=100)),
                ('past_harvests', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
                ('officer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Officer')),
            ],
        ),
    ]
