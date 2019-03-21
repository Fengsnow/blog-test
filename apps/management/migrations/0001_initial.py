# Generated by Django 2.1.7 on 2019-03-19 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Blog', max_length=50, verbose_name='网站标题')),
                ('name', models.CharField(default='开源博客', max_length=200, verbose_name='网站名称')),
                ('description', models.TextField(default='这是一个使用Vue+Django restful做的简单的个人博客。前端Vue主要用的amazeUI,Django的话，主要是reatframework和xadmin', max_length=1000, verbose_name='网站简介')),
                ('footer', models.CharField(default='Feng', max_length=50, verbose_name='页尾作者')),
                ('footerHtml', models.CharField(default='https://www.baidu.com', max_length=100, verbose_name='页尾链接')),
            ],
            options={
                'verbose_name': '站点信息',
                'verbose_name_plural': '站点信息',
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, default='card/default.jpg', upload_to='card/', verbose_name='轮播图')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('content', models.CharField(max_length=150, verbose_name='一句话')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '轮播卡片',
                'verbose_name_plural': '轮播卡片',
            },
        ),
    ]