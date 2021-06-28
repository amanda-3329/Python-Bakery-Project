from django.contrib import admin
from .models import Box, Order
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

# Register your models here.
admin.site.register(Order)
admin.site.register(Box)


class MapAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }