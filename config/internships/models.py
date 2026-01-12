from django.db import models

class Internship(models.Model):
    company = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
        related_name='internships'
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration_weeks = models.PositiveIntegerField()
    required_skills = models.ManyToManyField(
        'skills.Skill',
        related_name='internships'
    )
    min_match_percentage = models.PositiveIntegerField(default=50)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} at {self.company}"
