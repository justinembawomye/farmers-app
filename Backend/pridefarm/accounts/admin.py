from django.contrib import admin

# Register your models here.

from . models import Farmer, Officer, District, SubCounty, Harvest, Report, Season


@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display =('username', 'email',  'village')
   
@admin.register(Officer)
class OfficerAdmin(admin.ModelAdmin):
    list_display = ('login_id','firstname', 'lastname', 'phone_number', 'password', 'district', 'subcounty')

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('name','season', 'area', 'rice_type', 'sowing_date', 'sowing_type', 'Planting_type', 'Levelling', 'ridge', 'watercourse_state', 'fertilizers', 'weed_condition', 'harvest_date', 'total_harvest', 'note')



@admin.register(Harvest)
class HarvestAdmin(admin.ModelAdmin):
    list_display = ('name','season', 'area', 'Harvest')



@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name',)    



@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id','name')     

@admin.register(SubCounty)
class SubCountyAdmin(admin.ModelAdmin):
    list_display = ('name',)      