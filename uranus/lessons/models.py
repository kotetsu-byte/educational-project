from django.db import models

# Create your models here.
class Lesson(models.Model):
    title = models.TextField(null=True)
    info = models.TextField(null=True)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, null=True)