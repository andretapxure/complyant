from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_form, name='item_insert'),
    path('<int:id>/', views.item_form,name='item_update'),
    path('/delete/<int:id>', views.item_delete,name='item_delete'),
    path('list', views.item_list, name='item_list'),
]
