from django.contrib import admin
from .models import CustomUser

# Register your models here.
class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'wallet_address', 'is_active')
    list_filter = ('role',  'is_active')
    search_fields = ('username', 'email')
    ordering = ('username','email')