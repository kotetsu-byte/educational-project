from django.db import models

# Create your models here.
class Test(models.Model):
    question = models.CharField(null=True, max_length=255)
    answer1 = models.CharField(null=True, max_length=255)
    answer2 = models.CharField(null=True, max_length=255)
    answer3 = models.CharField(null=True, max_length=255)
    answer4 = models.CharField(null=True, max_length=255)
    correct_answer = models.IntegerField(null=True)
    points = models.IntegerField(null=True)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, null=True)