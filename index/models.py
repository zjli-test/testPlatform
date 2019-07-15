from django.db import models

# Create your models here.
class UserInfo(models.Model):
    #主键自增字段
    id = models.AutoField(primary_key=True)
    #创建不能为空的varchar类型数据
    name = models.CharField(null=False,max_length=20)