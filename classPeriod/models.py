from django.db import models;
from class_model.models import Classroom;
from course.models import Course;

class ClassPeriod(models.Model):
    start_time= models.TimeField()
    end_time = models.TimeField()
    classrooms = models.ManyToManyField(Classroom, related_name='class_Periods')
    courses = models.ManyToManyField(Course, related_name='class_Periods')
    day_of_week = models.DateField()

    def __str__(self):
        return f"{self.start_time} to {self.end_time}"
    
class ClassPeriodClassPeriod(models.Model):
    class_period = models.ForeignKey(ClassPeriod, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)