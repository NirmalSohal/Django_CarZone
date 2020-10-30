from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius : 50px;" />'.format(object.car_photo.url))
    
    thumbnail.short_description="Photo"

    list_display=('id','thumbnail','model','year','fuel_type','state','body_style','transmission','passengers','is_featured')
    search_fields=('model','year','fuel_type','state','body_style','transmission','passengers')
    list_display_links=('id','thumbnail','model')
    list_editable=('is_featured',)
    list_filter=('body_style','fuel_type','transmission','passengers')

admin.site.register(Car,CarAdmin)
