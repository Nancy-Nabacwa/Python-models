from rest_framework import serializers
from student.models import Student
from teacher.models import Teacher
from course.models import Course
from classPeriod.models import ClassPeriod
from class_model.models import Classroom
from datetime import datetime

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
        

class StudentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer( many = True )
    class Meta:
        model = Student
        # fields = "__all__"# fields cannot exist with exclude.
        exclude = ["email"]

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = "__all__"

class ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = "__all__"

class MinimalStudentSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    def get_full_name(self,object):
        return f"{object.first_name} {object.last_name}"
    
    def get_age(self,object):
        today = datetime.now()
        age = today - object.date_of_birth
        return age
    class Meta:
        model = Student
        fields = ["id","full_name","age","email"]

class MinimalTeacherSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    def get_full_name(self,object):
        return f"{object.first_name} {object.last_name}"
    
    class Meta:
        model = Teacher
        fields = ["id","full_name","email","assigned_classrooms"]
    

class MinimalCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_title', 'teacher', 'course_fee']

class MinimalClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['class_name','class_code', 'assigned_teachers']

