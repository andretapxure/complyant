from django.shortcuts import redirect, render
from .models import AssessmentItems, ComplianceLevel
from .forms import AssessmentItemsForm
def assessmentitems_form(request, id=0):
    if request.method == 'POST':
        if id == 0:
            form = AssessmentItemsForm(request.POST)
        else:
            assessmentitem = AssessmentItems.objects.get(pk=id)
            assessmentitem.compliance_level_id = request.POST['compliance_level_id']
            assessmentitem.measures = request.POST['measures']
            assessmentitem.reasonfornotapplicable = request.POST['reasonfornotapplicable']
            assessmentitem.save()
        return  redirect('assessment_fill', assessmentitem.assessment_id)