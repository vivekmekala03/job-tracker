from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):

    STATUS_CHOICES = [
        ('applied',    'Applied'),
        ('screening',  'Screening'),
        ('interview',  'Interview'),
        ('offer',      'Offer'),
        ('rejected',   'Rejected'),
    ]

    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    company      = models.CharField(max_length=200)
    role         = models.CharField(max_length=200)
    status       = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    date_applied = models.DateField(auto_now_add=True)
    job_url      = models.URLField(blank=True, null=True)
    notes        = models.TextField(blank=True)

    class Meta:
        ordering = ['-date_applied']

    def __str__(self):
        return f"{self.role} at {self.company} ({self.get_status_display()})"