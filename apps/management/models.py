from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class BlogSettings(models.Model):
    """
    站点信息
    """
    title = models.CharField(max_length=50,default="Blog",verbose_name="网站标题")
    name = models.CharField(max_length=200, default='开源博客',verbose_name="网站名称")
    description = models.TextField(max_length=1000, default="这是一个使用Vue+Django restful做的简单的个人博客。前端Vue主要用的amazeUI,Django的话，主要是reatframework和xadmin",verbose_name="网站简介" )
    footer = models.CharField(max_length=50,default='Feng',verbose_name="页尾作者")
    footerHtml = models.CharField(max_length=100,default='https://www.baidu.com',verbose_name="页尾链接")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '站点信息'
        verbose_name_plural = verbose_name

    def clean(self):
        if BlogSettings.objects.exclude(id=self.id).count():
            raise ValidationError(('只能有一个配置'))


class Card(models.Model):
    """
    轮播卡片
    """
    img = models.ImageField(upload_to="card/",blank=True, default="card/default.jpg", verbose_name='轮播图')
    title = models.CharField(max_length=50,verbose_name="标题")
    content = models.CharField(max_length=150, verbose_name='一句话')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '轮播卡片'
        verbose_name_plural = verbose_name