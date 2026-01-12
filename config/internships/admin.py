from django.contrib import admin
from .models import Internship

# Register your models here.
@admin.register(Internship)
class InternshipAdmin(admin.ModelAdmin):
    list_display = ('company', 'title', 'duration_weeks', 'min_match_percentage', 'is_active')
    list_filter = ('is_active', 'company')
    search_fields = ('company__username', 'title')
