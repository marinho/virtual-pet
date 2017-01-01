from django.contrib import admin

from .models import Being

class BeingAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth')

admin.site.register(Being, BeingAdmin)
