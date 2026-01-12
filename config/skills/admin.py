from django.contrib import admin
from .models import Skill,StudentSkill

# Register your models here.
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(StudentSkill)
class StudentSkillAdmin(admin.ModelAdmin):  
    list_display = ('student', 'skill', 'is_verified', 'verified_by', 'verified_at')
    list_filter = ('is_verified',)
    search_fields = ('student__username', 'skill__name')
