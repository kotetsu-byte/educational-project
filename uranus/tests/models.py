from django.db import models

# Create your models here.
class Test(models.Model):
    question = models.TextField(null=True)
    answer1 = models.TextField(null=True)
    answer2 = models.TextField(null=True)
    answer3 = models.TextField(null=True)
    answer4 = models.TextField(null=True)
    correct_answer = models.IntegerField(null=True)
    points = models.IntegerField(null=True)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, null=True)