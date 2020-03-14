from django.contrib import admin
from .models import User,Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=['user','father_name','mother_name','college_name','std_cell_no','parent_cell_no']
    class meta:
        model=Student

admin.site.register(Student,StudentAdmin)