# Generated by Django 2.2.14 on 2021-06-04 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20210604_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course',
        ),
        migrations.RemoveField(
            model_name='course',
            name='is_show_list',
        ),
        migrations.RemoveField(
            model_name='course',
            name='lesson',
        ),
        migrations.AddField(
            model_name='courselesson',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_lesson', to='course.Course', verbose_name='课程'),
        ),
        migrations.AddField(
            model_name='courselesson',
            name='is_show_list',
            field=models.BooleanField(default=False, verbose_name='是否推荐到课程列表'),
        ),
        migrations.AddField(
            model_name='courselesson',
            name='lesson',
            field=models.IntegerField(default=1, verbose_name='第几课时'),
        ),
    ]
