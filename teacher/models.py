from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    gender = models.TextField()
    email= models.EmailField()
    code = models.PositiveSmallIntegerField()
    country = models.TextField()
    bio = models.TextField()
    age = models.PositiveSmallIntegerField()
    phone_number = models.CharField(max_length = 20)
    qualifications = models.CharField(max_length = 20)
    hire_date = models.DateField()
    image = models.ImageField()


    def __str__(self):
        return f"{self.first_name} {self.last_name}"