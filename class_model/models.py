from django.db import models;


class Classroom(models.Model):
    class_name = models.CharField(max_length=20)
    class_code = models.PositiveSmallIntegerField()
    class_capacity = models.PositiveSmallIntegerField()
    class_duration = models.TimeField()
    class_training_assistant = models.CharField(max_length=20)
    class_representative = models.CharField(max_length=20)
    number_of_whiteboards = models.PositiveSmallIntegerField()
    number_of_tables = models.PositiveSmallIntegerField()
    number_of_chairs = models.PositiveSmallIntegerField()
    assigned_teachers = models.ManyToManyField('teacher.Teacher', related_name='classrooms_assigned')

    def __str__(self):
        return f"{self.class_name}"
