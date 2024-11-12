from django.db import models

# Create your models here.
from django.db import models


class User(models.Model):
    user = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    email = models.EmailField(unique=True)
    identity = models.BooleanField(default=False)

    def __str__(self):
        return self.user + " (T)" if self.identity else " (F)"


class Essay(models.Model):
    title = models.CharField(max_length=256)
    abstract = models.TextField()
    publish_year = models.IntegerField()
    category = models.CharField(max_length=16)
    features = models.BinaryField(default=b'')

    def __str__(self):
        return str(self.id) + " (" + str(self.category) + ")"


class Edge(models.Model):
    essay_id = models.IntegerField()
    cited_id = models.IntegerField()

    def __str__(self):
        return str(self.essay_id) + " -> " + str(self.cited_id)
