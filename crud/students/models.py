from django.db import models

# Create your models here.

class Grad (models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Lesson (models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Student (models.Model):
    name = models.CharField(max_length=50)
    grad = models.ForeignKey("Grad", verbose_name='grades', on_delete=models.CASCADE)
    lesson = models.ManyToManyField("lesson", verbose_name='lessons')

    def __str__(self):
        return self.name
