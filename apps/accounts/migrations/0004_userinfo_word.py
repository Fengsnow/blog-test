# Generated by Django 2.1.7 on 2019-03-19 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_userinfo_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='word',
            field=models.CharField(blank=True, max_length=100, verbose_name='简介'),
        ),
    ]
