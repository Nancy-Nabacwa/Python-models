from rest_framework.response import Response;
from rest_framework import status;
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
    
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetailView(APIView):
    def get(self,request,id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    def put(self,request,id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status = status.HTTP_202_ACCEPTED)


class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class TeacherDetailView(APIView):
    def get(self,request,id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    
    def put(self,request,id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status = status.HTTP_202_ACCEPTED)

class CourseListView(APIView):
    def get(self,request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many = True)
        return Response(serializer.data)
    def post(self,request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CourseDetailView(APIView):
    def get(self,request,id):
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    def put(self,request,id):
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        course = Course.objects.get(id=id)
        course.delete()
        return Response(status = status.HTTP_202_ACCEPTED)

class ClassroomListView(APIView):
    def get(self,request):
        classrooms = Classroom.objects.all()
        serializer = ClassroomSerializer(classrooms, many = True)
        return Response(serializer.data)
    def post(self,request):
        serializer = ClassroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ClassroomDetailView(APIView):
    def get(self,request,id):
        classroom = Classroom.objects.get(id=id)
        serializer = ClassroomSerializer(classroom)
        return Response(serializer.data)
    
    def put(self,request,id):
        classroom = Classroom.objects.get(id=id)
        serializer = ClassroomSerializer(classroom,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        classroom = Classroom.objects.get(id=id)
        classroom.delete()
        return Response(status = status.HTTP_202_ACCEPTED)
    
class ClassPeriodListView(APIView):
    def get(self,request):
        classPeriods = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classPeriods, many = True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ClassPeriodDetailView(APIView):
    def get(self,request,id):
        classPeriod = ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(classPeriod)
        return Response(serializer.data)
    
    def put(self,request,id):
        classPeriod = ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(classPeriod,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        classPeriod = ClassPeriod.objects.get(id=id)
        classPeriod.delete()
        return Response(status = status.HTTP_202_ACCEPTED)