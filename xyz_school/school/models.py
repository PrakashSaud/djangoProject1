from django.db import models

from office.models import School, Major
# Create your models here.

class Grade(models.Model):
    name=models.CharField(max_length=30)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    total_students=models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name=models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30)
    age=models.IntegerField()
    major=models.ForeignKey(Major, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.first_name + " "+self.middle_name+ " "+self.last_name

    def get_absolute_url(self):
        return "list"

