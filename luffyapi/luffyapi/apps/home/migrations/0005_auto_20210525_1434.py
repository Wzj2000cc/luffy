# Generated by Django 2.2.14 on 2021-05-25 14:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210525_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='添加数据的时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='banner',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, verbose_name='修改数据的时间'),
        ),
        migrations.AddField(
            model_name='nav',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='添加数据的时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nav',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, verbose_name='修改数据的时间'),
        ),
    ]
