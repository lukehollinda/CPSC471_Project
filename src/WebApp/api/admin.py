from django.contrib import admin
from .models import *


class LandAdmin(admin.ModelAdmin):
    list_display = ('address', 'postalCode', 'sqrAcres')

# Register your models here.

admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Land)
admin.site.register(Developer)
admin.site.register(Owner)
admin.site.register(PersonOwner)
admin.site.register(CompanyOwner)
admin.site.register(BankOwner)
admin.site.register(OwnsRelation)
admin.site.register(Building)
admin.site.register(CommercialBuilding)
admin.site.register(ResidentialBuilding)
admin.site.register(Renter)