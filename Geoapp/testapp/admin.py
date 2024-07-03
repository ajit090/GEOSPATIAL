from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import  Country


# Register your models here.
class CountryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display =  ['name', 'geometry']
    list_filter = ['name']

admin.site.register(Country,CountryAdmin)


