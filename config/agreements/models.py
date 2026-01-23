# agreements/models.py
from django.db import models
from django.conf import settings
from internships.models import Internship

User = settings.AUTH_USER_MODEL

class Agreement(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('COMPLETED', 'Completed'),
    )

    internship = models.ForeignKey(Internship, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    blockchain_tx_hash = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Transaction hash for on-chain agreement"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.internship} - {self.student}"
