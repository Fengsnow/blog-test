import xadmin
from .models import BlogSettings,Card




class CardAdmin(object):
    list_display = ["title", "content", "create_time"]
    model_icon = 'fa fa-photo'


class BlogSettingsAdmin(object):
    list_display = ["title","name", "description","footer"]
    model_icon = 'fa fa-steam'

xadmin.site.register(Card, CardAdmin)
xadmin.site.register(BlogSettings, BlogSettingsAdmin)
