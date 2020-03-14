from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

User=get_user_model()


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    father_name=models.CharField(max_length=64)
    mother_name=models.CharField(max_length=64)
    college_name=models.CharField(max_length=64)
    std_cell_no=models.BigIntegerField()
    parent_cell_no=models.BigIntegerField()

    def __str__(self):
        return str(self.user),self.father_name,self.mother_name

