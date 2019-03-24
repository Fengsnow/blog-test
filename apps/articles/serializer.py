from rest_framework import serializers

from .models import Category,Article,Tag

class CategorysSer(serializers.ModelSerializer):
    time = serializers.DateTimeField(source='create_time', format="%Y-%m-%d", required=False)
    parentName = serializers.CharField(source="parent_category.name",required=False)

    class Meta:
        model = Category
        fields = ["id","name","parentName","time"]


class TagsSer(serializers.ModelSerializer):
    time = serializers.DateTimeField(source='create_time', format="%Y-%m-%d", required=False)

    class Meta:
        model = Category
        fields = ["id","name","time"]

class HotArticlesSer(serializers.ModelSerializer):
    """
    热读文章
    """
    class Meta:
        model = Article
        fields = ["id","title",]



class TimeArticlesSer(serializers.ModelSerializer):
    """
    时间线
    """
    name = serializers.CharField(source='author.username', required=False, read_only=True)
    time = serializers.DateTimeField(source='create_time', format="%Y-%m-%d", required=False)
    categoryName = serializers.CharField(source='category.name', required=False, read_only=True)

    year = serializers.DateTimeField(source='create_time', format="%Y", required=False)
    month = serializers.DateTimeField(source='create_time', format="%m", required=False)
    class Meta:
        model = Article
        fields = ["id", "title","year","month","create_time" ,"time", "categoryName", "name"]


class CardArticlesSer(serializers.ModelSerializer):
    name = serializers.CharField(source='author.username', required=False, read_only=True)
    time = serializers.DateTimeField(source='comment_time', format="%Y-%m-%d", required=False)
    class Meta:
        model = Article
        fields = ["id","title","desc","img","name","time"]



class ArticlesSer(serializers.ModelSerializer):
    name = serializers.CharField(source='author.username', required=False, read_only=True)
    time = serializers.DateTimeField(source='create_time', format="%Y-%m-%d", required=False)
    categoryName = serializers.CharField(source='category.name',required=False, read_only=True)
    class Meta:
        model = Article
        fields = ["id","title","desc","img","views","comment_count","time","name","categoryName"]

class ArticlesDetailSer(serializers.ModelSerializer):
    name = serializers.CharField(source='author.username', required=False, read_only=True)
    avatar = serializers.ImageField(source='author.avatar', required=False, read_only=True)
    time = serializers.DateTimeField(source='create_time', format="%Y-%m-%d", required=False)
    categoryName = serializers.CharField(source='category.name',required=False, read_only=True)
    class Meta:
        model = Article
        fields = ["id","title","desc","detail","img","views","comment_count","time","name","avatar","categoryName","tags"]