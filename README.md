

#Xadmin的坑
(1)
Xadmin的安装，必须的保证是xadmin2.0的否则全线报错

(2)
Xadmin添加用户小组件出错render() got an unexpected keyword argument 'renderer

render函数在django2.1上有变化

   .进入xadmin安装路径，编辑xadmin/views/dashboard.py

 36     #render() got an unexpected keyword argument 'renderer'
 37     #修改bug, 添加renderer
 39     def render(self, name, value, attrs=None, renderer=None):