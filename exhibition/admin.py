from django.contrib import admin
from exhibition.models.exhibition import Exhibition

@admin.register(Exhibition)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'bunner', 'date', 'location',)