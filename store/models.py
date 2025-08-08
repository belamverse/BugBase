from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Repository(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    github_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Bug(models.Model):
    LABEL_CHOICES = [
        ('urgent', 'URGENT'),
        ('priority', 'PRIORITY'),
        ('low', 'LOW'),
    ]

    STATUS_CHOICES = [
        ('not_complete', 'Not Complete'),
        ('partially_completed', 'Partially Completed'),
        ('completed', 'Completed'),
    ]

    repository = models.ForeignKey(Repository, on_delete=models.CASCADE, related_name='bugs')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    issue = models.TextField()
    label = models.CharField(max_length=20, choices=LABEL_CHOICES, default='low')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='not_complete')
    due_date = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

