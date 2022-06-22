from django.contrib import admin
from .models import Customer

# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'companyName', 'active')


admin.site.register(Customer, CustomerAdmin)
