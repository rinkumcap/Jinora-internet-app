from django.contrib import admin

from .models import *
@admin.register(App)
class AppAdmin(admin.ModelAdmin):
   
    list_display = [field.name for field in App._meta.fields]   
