from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import IntrusionLog, KnownPerson

@admin.register(IntrusionLog)
class IntrusionLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'detected_person', 'image')
    list_filter = ('timestamp',)
    search_fields = ('detected_person',)

@admin.register(KnownPerson)
class KnownPersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    search_fields = ('name',)
