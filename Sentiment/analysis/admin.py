from django.contrib import admin
from .models import pages

# Register your models here.
@admin.register(pages)
class ActiveUserAdmin(admin.ModelAdmin):
    list_display = ['page_name']