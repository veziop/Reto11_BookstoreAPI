from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Author(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    created_date = models.DateField(default=timezone.now)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_date = models.DateField(default=timezone.now)
    added_by_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

