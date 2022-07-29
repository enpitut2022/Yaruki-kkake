from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Rank(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.CharField(max_length=100)

    def __str__(self):
        return self.time