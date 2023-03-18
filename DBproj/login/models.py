from django.db import models

class Account(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=25)
    keyword = models.CharField(max_length=25)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.name}'
    class Meta:
        db_table = 'accounts'
        
        
class Admin_account(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.CharField(max_length=25, unique=True)
    is_staff=models.BooleanField(default='True')
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=25)
    create_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        db_table = 'Admin_account'