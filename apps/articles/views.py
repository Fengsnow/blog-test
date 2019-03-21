from rest_framework import mixins,filters,viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Category,Article,Tag
from .serializer import CategorysSer,ArticlesSer,TagsSer,HotArticlesSer,CardArticlesSer

class ArticlesPage(PageNumberPagination):
    page_size = 6
    max_page_size = 10

class CategorysViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    文章分类列表
    """
    queryset = Category.objects.all()
    serializer_class = CategorysSer

class TagsViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    标签列表
    """
    queryset = Tag.objects.all()
    serializer_class = TagsSer

class ArticlesViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    文章列表页, 分页， 搜索， 过滤， 排序
    """
    queryset = Article.objects.filter(status=1).order_by("-create_time")
    serializer_class = ArticlesSer
    pagination_class = ArticlesPage
    #filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    #filter_class = GoodsFilter

class HotArticleSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    热读文章，前5个
    """
    queryset = Article.objects.filter(status=1).order_by("-views")[:5]
    serializer_class = HotArticlesSer


class CardArticleSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    置顶轮播
    """
    queryset = Article.objects.filter(top=1)
    serializer_class = CardArticlesSer
