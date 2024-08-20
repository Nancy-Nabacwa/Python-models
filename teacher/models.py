from django.db import models 
from course.models import Course

class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    email = models.EmailField()
    code = models.PositiveSmallIntegerField()
    country = models.CharField(max_length=20)
    bio = models.TextField()
    age = models.PositiveSmallIntegerField()
    phone_number = models.CharField(max_length=20)
    teacher_salary = models.PositiveSmallIntegerField(default=0)
    hire_date = models.DateField()
    image = models.ImageField(blank=True ,null=True)
    assigned_classrooms = models.ManyToManyField('class_model.Classroom', related_name='teachers_assigned')  
    courses = models.ManyToManyField(Course, related_name='teachers')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"