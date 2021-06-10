# Generated by Django 2.2.14 on 2021-06-10 09:35

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20210604_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_video',
            field=models.FileField(blank=True, null=True, upload_to='video', verbose_name='视频'),
        ),
        migrations.AlterField(
            model_name='course',
            name='brief',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=2048, null=True, verbose_name='详情介绍'),
        ),
    ]
