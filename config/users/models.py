from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('STUDENT', 'student'),
        ('COMPANY', 'company'),
        ('UNIVERSITY', 'university'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='STUDENT')
    wallet_address = models.CharField(max_length=255, blank=True, null=True,
        help_text="Blockchain wallet address (e.g., MetaMask)")

    def __str__(self):
        return f"{self.username} ({self.role})"