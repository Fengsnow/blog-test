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

    class Meta:
        model = Article
        fields = ["id","title",]

class CardArticlesSer(serializers.ModelSerializer):
    name = serializers.CharField(source='author.username', required=False, read_only=True)
    time = serializers.DateTimeField(source='comment_time', format="%Y-%m-%d", required=False)
    class Meta:
        model = Article
        fields = ["id","title","desc","img","name","time"]

class ArticlesSer(serializers.ModelSerializer):
    name = serializers.CharField(source='author.username', required=False, read_only=True)
    time = serializers.DateTimeField(source='comment_time', format="%Y-%m-%d", required=False)
    categoryName = serializers.CharField(source='category.name',required=False, read_only=True)
    class Meta:
        model = Article
        fields = ["id","title","desc","img","views","comment_count","time","name","categoryName"]