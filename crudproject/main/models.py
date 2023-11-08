from django.db import models

# Create your models here.
class ToDoStuff(models.Model):
    stuff = models.CharField(max_length=500)
    detail = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.stuff
    