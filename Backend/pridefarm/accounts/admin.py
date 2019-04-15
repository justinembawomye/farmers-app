from django.contrib import admin

# Register your models here.

from . models import Farmer, Officer, District, SubCounty

admin.site.register(Farmer)
admin.site.register(Officer)
admin.site.register(SubCounty)
admin.site.register(District)