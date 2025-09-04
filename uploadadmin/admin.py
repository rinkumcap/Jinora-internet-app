from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(AdminUser)
class SuperAdmin(admin.ModelAdmin):
   
    list_display = [field.name for field in AdminUser._meta.fields]   
