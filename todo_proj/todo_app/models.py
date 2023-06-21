from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):

    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('pending', 'Pending'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_date = models.DateField(auto_now_add=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    user = models.ForeignKey('accounts.User',on_delete=models.CASCADE)

    def __str__(self):
        return self.title


