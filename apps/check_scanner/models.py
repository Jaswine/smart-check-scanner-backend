import uuid

from django.contrib.auth.models import User
from django.db import models

class CheckQuerySet(models.QuerySet):
    def all(self):
        return self.filter(is_active=True)

class Check(models.Model):
    """
        Check model for document scanning and recommendation generation.
    """
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def file_directory_path(self, filename):
        extension = filename.split('.')[-1]
        new_filename = f'{self.id}_document_{uuid.uuid4().hex[:10]}.{extension}'
        return f'files/{self.user.username}/uploaded-files/{new_filename}'

    file = models.FileField(upload_to=file_directory_path)
    extracted_text = models.TextField(blank=True)

    recommendations = models.TextField(blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return f'{self.user} - {self.id} - {self.status}'
