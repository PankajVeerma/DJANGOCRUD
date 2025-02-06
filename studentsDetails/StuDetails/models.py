from django.db import models
import uuid

# Create your models here.
class StudentData(models.Model):
  id = models.AutoField(primary_key=True)
 
  studentName =models.CharField( max_length=50,blank=False,null=False)
  email=models.EmailField()
  branch=models.CharField(max_length=50,blank=False,null=False)
  year=models.DateField( auto_now=False, auto_now_add=False)
  language = models.CharField(max_length=100, blank=False, null=True)
  
def __str__(self):
    return self.studentName
