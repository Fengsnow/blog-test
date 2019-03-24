import xadmin
from django.contrib import admin
from django.db.models import F
from .models import Category,Article,Tag
from bs4 import BeautifulSoup

class ArticleAdmin(object):
    list_display = ["title", "desc", "top","status","count", "views", "comment_count",
                   "create_time", "author", "category"]
    search_fields = ['title', ]

    readonly_fields=["desc","count","create_time"]
    exclude = ["author", "img","views", "comment_count", "comment_time"]

    list_filter = ["title", "category", "author", "status"]

    model_icon = 'fa fa-edit'

    def save_models(self):
        obj = self.new_obj
        flag = self.org_obj is None and 'create' or 'change'
        soup = BeautifulSoup(obj.detail, "html.parser")
        obj.desc = soup.text[0:100]
        img = None
        for tag in soup.find_all('img'):
            if tag:
                img_url = tag.get('src')
                img = img_url[7:]
                print(img)
                break
        if img:
            obj.img = img

        if flag == 'create':
            obj.author = self.request.user
        else:
            obj.count = F('count')+1
        #obj.author = request.user
        obj.save()


class CategoryAdmin(object):
    list_display = ["name", "parent_category", "create_time"]
    list_filter = ["parent_category"]
    search_fields = ['name', ]
    model_icon = 'fa fa-list-ol'


class TagAdmin(object):
    list_display = ["name", "create_time"]
    model_icon = 'fa fa-tags'

xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Tag, TagAdmin)
