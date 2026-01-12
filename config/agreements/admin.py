from django.contrib import admin
from .models import Agreement

# Register your models here.
@ admin.register(Agreement)
class AgreementAdmin(admin.ModelAdmin):
    list_display =('student', 'company', 'internship', 'start_date', 'end_date', 'status')
    list_filter = ('status', 'company', 'student')
