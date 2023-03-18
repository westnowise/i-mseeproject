from django.db import models
from login.models import Admin_account


# class ExhibitionDetail(models.Model):
#     exhibition_id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=50)
#     image = models.ImageField(max_length=255,upload_to='images/', blank=True, null=True)
#     camera = models.CharField(max_length=20, blank=True, null=True)
#     place = models.CharField(max_length=200, blank=True, null=True)
#     info = models.CharField(max_length=2000, blank=True, null=True)
#     cost = models.PositiveIntegerField(blank=True, null=True)
#     link = models.CharField(max_length=200, blank=True, null=True)
#     # count = models.PositiveIntegerField(blank=True, null=True)
#     keyword = models.CharField(max_length=10, blank=True, null=True)

#     def __str__(self):
#         return self.title
#     # like_count = models.PositiveIntegerFied(default=0)
    
#     class Meta:
#         # managed = True
#         db_table = 'exhibition_detail'
        
        
# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     keyword = models.CharField(max_length=10, db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'user'


class ExhibitionDetail(models.Model):
    exhibition_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    image = models.ImageField(max_length=255,upload_to='images/', blank=True, null=True)
    camera = models.CharField(max_length=20, blank=True, null=True)
    place = models.CharField(max_length=200, blank=True, null=True)
    info = models.CharField(max_length=2000, blank=True, null=True)
    cost = models.PositiveIntegerField(blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    keyword = models.CharField(max_length=10, blank=True, null=True)
    # admin = models.ForeignKey(AdminAccount, models.DO_NOTHING, blank=True, null=True, on_delete=models.CASCADE)
    admin=models.ForeignKey(Admin_account, null=True, on_delete=models.CASCADE) #admin이 삭제되면 디테일도 함께 삭제됨.
    
    class Meta:
        managed = True
        db_table = 'exhibition_detail'