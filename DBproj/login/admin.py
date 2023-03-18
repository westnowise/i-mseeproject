from django.contrib import admin
from .models import Account,Admin_account
# Register your models here.

@admin.register(Account)
class Account(admin.ModelAdmin):
    list_display = (
        'userid',
        'password',
        'name',
        'keyword',
    )
    
@admin.register(Admin_account)
class Admin_account(admin.ModelAdmin):
    list_display = (
        'userid',
        'password',
        'name'
    )