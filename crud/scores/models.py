from django.db import models
from students.models import Student
# Create your models here.

class Score(models.Model):    
    student = models.ForeignKey(Student, related_name='scores', on_delete=models.CASCADE)
    score = models.IntegerField(null=True, default=5)

    def __str__(self):
        return f"Student : {self.student} - Score : {self.score}"
