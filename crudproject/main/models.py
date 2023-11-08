from django.db import models

# Create your models here.
class ToDoStuff(models.Model):
    stuff = models.CharField(max_length=500)

    def __str__(self):
        return self.stuff
    