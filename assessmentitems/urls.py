from django.urls import path
from . import views

urlpatterns = [
    path('', views.assessmentitems_form, name='assessmentitems_insert'),
    path('<int:id>', views.assessmentitems_form,name='assessmentitems_update'),
]
