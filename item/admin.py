from django.contrib import admin
from .models import Item, Category, RiskType


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Category, CategoryAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'risk', 'category')


admin.site.register(Item, ItemAdmin)

class RiskTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(RiskType, RiskTypeAdmin)
