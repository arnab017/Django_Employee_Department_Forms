from django.db import models

# Create your models here.

class Dept(models.Model):
    dept_no = models.IntegerField(primary_key=True)
    dept_name = models.CharField(max_length=30)
    loc = models.CharField(max_length=30)
    
    def __str__(self):
        return str(self.dept_no)

class Emp(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=50)
    job = models.CharField(max_length=30)
    sal = models.IntegerField()
    hire_date = models.DateField()
    dept_no = models.ForeignKey(Dept, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.emp_name
    