from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserInfo(AbstractUser):
    """
    用户表
    """
    word = models.CharField(max_length=100,blank=True,verbose_name='简介')
    avatar = models.ImageField(upload_to="avatars/",blank=True, verbose_name='头像')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username