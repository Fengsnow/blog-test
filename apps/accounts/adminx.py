import xadmin
from xadmin import views

class BaseSetting(object):
    enable_themes = False  # 开启主题切换功能
    use_bootswatch = True

class GlobalSettings(object):
    site_title = "Blog后台"
    site_footer = "MyBlog"
    # menu_style = "accordion" #菜单折叠


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)