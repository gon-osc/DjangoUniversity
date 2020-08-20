from django.db import models

# Create your models here.

class djangoClasses(models.Model):
    Title = models.CharField(max_length=60)
    Course_Number = models.IntegerField(default=None, blank=True,null=False)
    Instructor_Name = models.CharField(max_length=100, blank=True, null=False)
    Duration = models.CharField(max_length=60, default=None, blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.Title