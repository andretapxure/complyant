from django.shortcuts import redirect, render
from .forms import AssessmentForm
from .models import Assessment


def assessment_list(request):
    context = {'assessments': Assessment.objects.all()}
    return render(request, "assessment/assessment_list.html", context)


def assessment_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = AssessmentForm()
        else:
            assessment = Assessment.objects.get(pk=id)
            form = AssessmentForm(instance=assessment)
        return render(request, "assessment/assessment_form.html", {'form': form})
    if request.method == 'POST':
        if id == 0:
            form = AssessmentForm(request.POST)
        else:
            assessment = Assessment.objects.get(pk=id)
            form = AssessmentForm(request.POST, instance=assessment)
        if form.is_valid():
            form.save()
        return redirect('/assessment/list')


def assessment_delete(request, id):
    assessment = Assessment.objects.get(pk=id)
    assessment.delete
    return redirect('/assessment/list')
