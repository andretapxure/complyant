from django.contrib import admin
from .models import Assessment

# Register your models here.
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('customer', 'date', 'template')

admin.site.register(Assessment, AssessmentAdmin)
