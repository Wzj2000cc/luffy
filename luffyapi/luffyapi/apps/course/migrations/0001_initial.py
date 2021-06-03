# Generated by Django 2.2.14 on 2021-06-03 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否显示')),
                ('orders', models.IntegerField(default=1, verbose_name='排序')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加数据的时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='修改数据的时间')),
                ('name', models.CharField(max_length=128, verbose_name='课程名称')),
                ('course_img', models.ImageField(blank=True, max_length=255, null=True, upload_to='course', verbose_name='封面图片')),
                ('course_type', models.SmallIntegerField(choices=[(0, '付费'), (1, 'VIP专享'), (2, '学位课程')], default=0, verbose_name='付费类型')),
                ('brief', models.TextField(blank=True, max_length=2048, null=True, verbose_name='详情介绍')),
                ('level', models.SmallIntegerField(choices=[(0, '初级'), (1, '中级'), (2, '高级')], default=1, verbose_name='难度等级')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='发布日期')),
                ('period', models.IntegerField(default=7, verbose_name='建议学习周期(day)')),
                ('attachment_path', models.FileField(blank=True, max_length=128, null=True, upload_to='', verbose_name='课件路径')),
                ('status', models.SmallIntegerField(choices=[(0, '上线'), (1, '下线'), (2, '预上线')], default=0, verbose_name='课程状态')),
                ('students', models.IntegerField(default=0, verbose_name='学习人数')),
                ('lessons', models.IntegerField(default=0, verbose_name='总课时数量')),
                ('pub_lessons', models.IntegerField(default=0, verbose_name='课时更新数量')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='课程原价')),
            ],
            options={
                'db_table': 'ly_course',
            },
        ),
        migrations.CreateModel(
            name='CourseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否显示')),
                ('orders', models.IntegerField(default=1, verbose_name='排序')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加数据的时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='修改数据的时间')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='分类课程名称')),
            ],
            options={
                'verbose_name': '课程分类',
                'verbose_name_plural': '课程分类',
                'db_table': 'ly_course_category',
            },
        ),
        migrations.CreateModel(
            name='CourseChapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否显示')),
                ('orders', models.IntegerField(default=1, verbose_name='排序')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加数据的时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='修改数据的时间')),
                ('chapter', models.SmallIntegerField(default=1, verbose_name='第几章')),
                ('name', models.CharField(max_length=128, verbose_name='章节标题')),
                ('summary', models.TextField(blank=True, null=True, verbose_name='章节介绍')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='发布日期')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coursechapters', to='course.Course', verbose_name='课程名称')),
            ],
            options={
                'verbose_name': '课程章节',
                'verbose_name_plural': '课程章节',
                'db_table': 'ly_course_chapter',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否显示')),
                ('orders', models.IntegerField(default=1, verbose_name='排序')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加数据的时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='修改数据的时间')),
                ('name', models.CharField(max_length=32, verbose_name='讲师title')),
                ('role', models.SmallIntegerField(choices=[(0, '讲师'), (1, '导师'), (2, '班主任')], default=0, verbose_name='讲师身份')),
                ('title', models.CharField(max_length=64, verbose_name='职位、职称')),
                ('signature', models.CharField(blank=True, help_text='导师签名', max_length=255, null=True, verbose_name='导师签名')),
                ('image', models.ImageField(null=True, upload_to='teacher', verbose_name='讲师封面')),
                ('brief', models.TextField(max_length=1024, verbose_name='讲师描述')),
            ],
            options={
                'verbose_name': '讲师导师',
                'verbose_name_plural': '讲师导师',
                'db_table': 'ly_teacher',
            },
        ),
        migrations.CreateModel(
            name='CourseLesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否显示')),
                ('orders', models.IntegerField(default=1, verbose_name='排序')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加数据的时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='修改数据的时间')),
                ('name', models.CharField(max_length=128, verbose_name='课时标题')),
                ('section_type', models.SmallIntegerField(choices=[(0, '文档'), (1, '练习'), (2, '视频')], default=2, verbose_name='课时种类')),
                ('section_link', models.CharField(blank=True, help_text='若是video，填vid,若是文档，填link', max_length=255, null=True, verbose_name='课时链接')),
                ('duration', models.CharField(blank=True, max_length=32, null=True, verbose_name='视频时长')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('free_trail', models.BooleanField(default=False, verbose_name='是否可试看')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coursesections', to='course.CourseChapter', verbose_name='课程章节')),
            ],
            options={
                'verbose_name': '课程课时',
                'verbose_name_plural': '课程课时',
                'db_table': 'ly_course_lesson',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='course_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.CourseCategory', verbose_name='课程分类'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='course.Teacher', verbose_name='授课老师'),
        ),
    ]
