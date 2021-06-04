from rest_framework import serializers
from . import models


class CourseCategoryModelSerializer(serializers.ModelSerializer):
    """ 展示课程列表的序列化器"""
    class Meta:
        model = models.CourseCategory
        fields = ['id', 'name']

# 老师表序列化器
class TeacherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ['name', 'title', 'signature']


"""
展示课程详细信息 + 老师信息 + 课时信息 
    序列化器获取其他表数据
"""
class CourseModelSerializer(serializers.ModelSerializer):

    # 方式一：直接关系
    # teacher_name = serializers.CharField(max_length=32,source='teacher.name')

    # 方式二：
    # 课程对老师是多对一，老师是一
    teacher=  TeacherModelSerializer()
    # 老师对课程是多对一，老师是多
    # teacher=  TeacherModelSerializer(many=True)

    class Meta:
        model = models.Course
        fields = ["id", "name", "course_img", "students", "lessons", "pub_lessons", "price",'teacher','lesson_list']