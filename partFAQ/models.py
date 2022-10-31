from django.db import models

# Create your models here.
class FAQContent(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    def __str__(self):
        return self.question
