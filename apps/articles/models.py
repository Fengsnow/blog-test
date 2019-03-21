from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from accounts.models import UserInfo
# Create your models here.


class Category(models.Model):
    """
    文章分类
    """
    name = models.CharField(max_length=30, unique=True,verbose_name="分类名")
    parent_category = models.ForeignKey("self", null=True, blank=True, help_text="父目录",
                                        related_name="parent", on_delete=models.CASCADE, verbose_name="父类级别")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, null=True,verbose_name="更新时间")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "文章分类"
        verbose_name_plural = verbose_name

class Tag(models.Model):
    """
    标签
    """
    name = models.CharField(max_length=30, unique=True,verbose_name="标签名")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name


class Article(models.Model):
    """
    文章
    """
    status_choice = (
        (0, "草稿"),
        (1, "发表"),
    )
    top_choice = (
        (0, "普通"),
        (1, "置顶"),
    )

    title = models.CharField(max_length=100,verbose_name="标题")
    detail = RichTextUploadingField(verbose_name="内容",)
    desc = models.CharField(max_length=300, blank=True,verbose_name='简介')
    img = models.ImageField(upload_to="upload/",blank=True, default="upload/default.jpg", verbose_name='图片')
    status = models.IntegerField(choices=status_choice, default=0,verbose_name="状态")
    top = models.IntegerField(choices=top_choice,default=0,blank=True,verbose_name="置顶")
    views = models.IntegerField(default=0,verbose_name="阅读量")
    comment_count = models.IntegerField(default=0,verbose_name="评论数")
    count = models.IntegerField(default=0,verbose_name="修改次数")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    comment_time = models.DateTimeField(auto_now=True, blank=True,verbose_name="更新时间")

    author = models.ForeignKey(UserInfo,on_delete=models.CASCADE,blank=True,verbose_name="作者")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    tags = models.ManyToManyField(Tag, verbose_name='标签集合', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name