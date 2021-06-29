from django.contrib import admin
from searchapp.models import Product

from import_export.admin import ImportExportModelAdmin
# class DataAdmin(admin.ModelAdmin):
    # list_display = ['data']

# admin.site.register(Data,DataAdmin)

@admin.register(Product)
class ViewAdmin(ImportExportModelAdmin):
    pass
