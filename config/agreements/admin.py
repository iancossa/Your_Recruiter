from django.contrib import admin
from .models import Agreement

# Register your models here.
@ admin.register(Agreement)
class AgreementAdmin(admin.ModelAdmin):
    list_display =('student',  'internship', 'status')
    list_filter = ('status',)
