from django.db import models

# Create your models here.

class Score(models.Model):
    name = models.CharField(max_length=50, null=True)
    score = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.name} - Score : {self.score}"
