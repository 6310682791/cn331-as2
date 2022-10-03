from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Course(models.Model):
    sub_name = models.CharField(max_length= 64)
    sub_code = models.CharField(max_length= 5)
    semester = models.IntegerField(default=1)
    year = models.IntegerField(default=2022)
    max_seat = models.IntegerField(default=0)
    registered = models.ManyToManyField(User, blank= True, related_name="subjects")


    def __str__(self):
        return f"{self.semester}/{self.year}: ({self.sub_code}) {self.sub_name}"



class Enrollment(models.Model):
    user = models.ManyToManyField(User)
    courses = models.ForeignKey(Course, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.courses}"

