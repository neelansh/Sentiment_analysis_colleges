from django.contrib import admin
from .models import pages, tweets, twitter, fullform

# Register your models here.
@admin.register(pages)
class ActiveUserAdmin(admin.ModelAdmin):
    list_display = ['page_name']

@admin.register(twitter)
class ActiveUserAdmin(admin.ModelAdmin):
    list_display = ['institute_name']

@admin.register(tweets)
class ActiveUserAdmin(admin.ModelAdmin):
    list_display = ['user_name']

@admin.register(fullform)
class ActiveUserAdmin(admin.ModelAdmin):
    list_display = ['short_form' , 'full_form']