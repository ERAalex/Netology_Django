from django.contrib import admin
from .models import Phone



@admin.register(Phone)
class phone_Admin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['lte_exists', 'name']