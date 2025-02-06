from django.contrib import admin
from .models import StudentData


# Register your models here.


class studentDetails(admin.ModelAdmin):
  list_display = ['studentName','email','branch','year','language']

admin.site.register(StudentData,studentDetails)  