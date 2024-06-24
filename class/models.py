from django.db import models

class Class(models.Model):
    class_name = models.CharField(max_length = 20)
    class_code = models.PositiveSmallIntegerField()
    class_capacity = models.PositiveSmallIntegerField()
    class_duration= models.TimeField()
    class_training_assistant = models.CharField(max_length = 20)
    class_representative = models.CharField(max_length = 20)
    teacher_code = models.ForeignKey('Teacher', on_delete = models.CASCADE)
    number_of_whiteboards = models.PositiveSmallIntegerField()
    number_of_tables = models.PositiveSmallIntegerField()
    number_of_chairs = models.PositiveSmallIntegerField()
    
    


    def __str__(self):
        return f"{self.class_name} {self.class_schedule}"
