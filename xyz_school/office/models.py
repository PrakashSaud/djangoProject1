from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=200)
    address =models.CharField(max_length=400)

    class Meta:
        verbose_name_plural='school'

    def __str__(self) -> str:
        return self.name + "\n"+ self.address

class Major(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.name