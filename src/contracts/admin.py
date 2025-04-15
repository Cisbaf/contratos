from django.contrib import admin
from .models import Sector, Contract

class SectorAdmin(admin.ModelAdmin):
    pass


class DataUserAdmin(admin.ModelAdmin):
    pass


class ContractAdmin(admin.ModelAdmin):
    pass


admin.site.register(Sector, SectorAdmin)
admin.site.register(Contract, ContractAdmin)