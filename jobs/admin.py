from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display  = ('company', 'role', 'status', 'date_applied', 'user')
    list_filter   = ('status',)
    search_fields = ('company', 'role')