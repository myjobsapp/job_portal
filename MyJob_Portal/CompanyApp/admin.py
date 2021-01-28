from django.contrib import admin
from .models import CompanyModel,JobModel

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name','loc','type','domain']
admin.site.register(CompanyModel,CompanyAdmin)


class JobAdmin(admin.ModelAdmin):
    list_display = ['desg','ctc','exp','loc','skills']
admin.site.register(JobModel,JobAdmin)
