from django.contrib import admin
from .models import AssessmentItems, ComplianceLevel

# Register your models here.
class AssessmentItemsAdmin(admin.ModelAdmin):
    readonly_fields = ('item',)
    list_display = ('assessment','item','compliance_level_id', 'measures')
    list_filter = ('assessment', 'compliance_level', 'item')
admin.site.register(AssessmentItems, AssessmentItemsAdmin)

class ComplianceLevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(ComplianceLevel, ComplianceLevelAdmin)
