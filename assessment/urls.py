from django.urls import path
from . import views

urlpatterns = [
    path('', views.assessment_form, name='assessment_insert'),
    path('<int:id>', views.assessment_form,name='assessment_update'),
    path('/delete/<int:id>', views.assessment_delete,name='assessment_delete'),
    path('list', views.assessment_list, name='assessment_list'),
    path('fill/<int:id>', views.assessment_fill, name='assessment_fill'),
]
