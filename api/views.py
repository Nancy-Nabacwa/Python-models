from rest_framework.response import Response;
from rest_framework.views import APIView;
from student.models import Student;
from teacher.models import Teacher;
from course.models import Course;
from classPeriod.models import ClassPeriod;
from class_model.models import Classroom;
from .serializers import StudentSerializer;
from .serializers import TeacherSerializer
from .serializers import CourseSerializer;
from .serializers import ClassroomSerializer;
from .serializers import ClassPeriodSerializer;

class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many = True)
        return Response(serializer.data)

class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

class CourseListView(APIView):
    def get(self,request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many = True)
        return Response(serializer.data)

class ClassroomListView(APIView):
    def get(self,request):
        classrooms = Classroom.objects.all()
        serializer = ClassroomSerializer(classrooms, many = True)
        return Response(serializer.data)
    
class ClassPeriodListView(APIView):
    def get(self,request):
        classPeriods = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classPeriods, many = True)
        return Response(serializer.data)