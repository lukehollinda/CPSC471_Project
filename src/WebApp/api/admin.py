from django.contrib import admin
from .models import Land


class LandAdmin(admin.ModelAdmin):
    list_display = ('address', 'postalCode', 'sqrAcres')

# Register your models here.

admin.site.register(Land)