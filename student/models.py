from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email= models.EmailField()
    student_code = models.PositiveSmallIntegerField()
    date_of_birth = models.DateField()
    country = models.CharField(max_length = 20)
    bio = models.TextField()
    age = models.PositiveSmallIntegerField()
    phone_number = models.CharField(max_length = 20)
    immediate_contact = models.CharField(max_length = 20)
    image = models.ImageField()
    class_code = models.ForeignKey('Class' ,on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
