from django.contrib import admin
from empapp.models import Emp

# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_diplay = ['id','first_name', 'last_name']
    list_filter = ['first_name']


admin.site.register(Emp, EmpAdmin)