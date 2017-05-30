from django.contrib import admin
from .models import Colors
# Register your models here.
admin.site.register(Colors)

from .forms import ColorsForm

class ColorsAdmin(admin.ModelAdmin):
    form = ColorsForm
    fieldsets = (
        (None, {
            'fields': ('color')
            }),
        )