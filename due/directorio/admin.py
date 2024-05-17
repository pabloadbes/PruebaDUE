from django.contrib import admin
from .models import Company

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
   readonly_fields = ('created', 'updated')
   list_display = ('cuit', 'company_name', 'activity_code', 'city', 'created', 'updated')
   ordering = ('activity_code', 'company_name')
   search_fields = ('cuit', 'company_name', 'activity_code')
   list_filter = ('activity_code', 'city')

admin.site.register(Company, CompanyAdmin)