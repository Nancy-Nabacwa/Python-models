from django.db import models

class Class(models.Model):
    class_name = models.TextField()
    class_capacity = models.PositiveSmallIntegerField()
    class_schedule= models.TextField()
    class_projects = models.TextField()
    class_activities = models.TextField()
    class_representative = models.TextField()
    class_assignments = models.TextField()
    class_policies = models.TextField()
    class_requirements = models.TextField()
    class_members_images = models.ImageField()


    def __str__(self):
        return f"{self.class_name} {self.class_schedule}"
