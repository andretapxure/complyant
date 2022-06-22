from django.contrib import admin
from .models import Template

# Register your models here.
class TemplateAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Template, TemplateAdmin)
