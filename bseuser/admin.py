from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields

class StateResource(resources.ModelResource):

    class Meta:
        model = State
        import_id_fields = ('name','country','code')

class StateAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    resource_class = StateResource


class CityResource(resources.ModelResource):

    class Meta:
        model = City
        import_id_fields = ('state','country','name')

class CityAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    resource_class = CityResource


class CountryResource(resources.ModelResource):

    class Meta:
        model = Country
        import_id_fields = ('name', 'code',)

class CountryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'code')
    resource_class = CountryResource


admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Clientmaster)
admin.site.register(Bankmaster)
admin.site.register(Demat)
admin.site.register(Branchmaster)
admin.site.register(Designation)
admin.site.register(Employeemaster)
admin.site.register(Address)
admin.site.register(Superdistributor)
admin.site.register(Distributor)
admin.site.register(Referencemaster)