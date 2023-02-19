from django.contrib import admin
from .models import *
# Register your models here.

class CategoriesHolidayAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender']


class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'categories', 'price', 'data_start', 'data_end', 'is_active']
    list_filter = ['categories', 'is_active', 'popular']
    search_fields = ['name', 'price']


admin.site.register(CategoriesHoliday, CategoriesHolidayAdmin)
admin.site.register(Event, EventAdmin)

