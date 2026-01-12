from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class StudentSkill(models.Model):
    student = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE,related_name='skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    verified_by = models.ForeignKey(
        User,
        on_deletee=models.SET_NULL,
        null=True,
        blank=True,
        related_name='verified_skills'
    )

    verified_at: models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return f"{self.student} - {self.skill}"
    