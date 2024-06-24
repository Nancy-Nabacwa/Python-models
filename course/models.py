from django.db import models

class Course(models.Model):
    course_title = models.CharField(max_length = 20)
    course_category = models.CharField(max_length = 20)
    course_start_date = models.DateField()
    course_end_date= models.DateField()
    course_code = models.PositiveSmallIntegerField()
    teacher_code = models.ForeignKey('Teacher', on_delete = models.CASCADE)
    maximum_attendees = models.PositiveSmallIntegerField()
    course_level= models.CharField(max_length = 20)
    student_code = models.ForeignKey('Student', on_delete = models.CASCADE)
    course_fee = models.PositiveSmallIntegerField()
   
    def __str__(self):
        return f"{self.course_title} {self.course_category}"
