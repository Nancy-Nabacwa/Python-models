from django.db.models import Prefetch;
from rest_framework.response import Response;
from rest_framework import status;
from rest_framework.views import APIView;
from student.models import Student;
from teacher.models import Teacher;
from course.models import Course;
from classPeriod.models import ClassPeriod, ClassPeriodClassPeriod;
from class_model.models import Classroom;
from .serializers import StudentSerializer;
from .serializers import TeacherSerializer
from .serializers import CourseSerializer;
from .serializers import ClassroomSerializer;
from .serializers import ClassPeriodSerializer;


class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        first_name = request.query_params.get("first_name")
        country = request.query_params.get("country")
        if first_name:
            students = students.filter(first_name = first_name)
        if country:
            country = students.filter(country = country)
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
    def enroll(self,student,course_code):
        course = Course.objects.get(id=course_code)
        student.courses.add(course)

    def post(self,request,id):
        student = Student.objects.get(id=id)
        action = request.data.get("action")
        if action == "enroll":
            course_code = request.data.get("course_code")
            self.enroll(student,course_code)
        return Response(status=status.HTTP_201_CREATED)
    
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
    def assign_course(self, teacher, course_code):
        course = Course.objects.get(id=course_code)
        teacher.courses.add(course)

    def assign_class(self, teacher, class_code):
        classroom = Classroom.objects.get(id=class_code)
        teacher.assigned_classrooms.add(classroom)
    
    def post(self, request, id):
        teacher = Teacher.objects.get(id=id)
        action = request.data.get("action")
        if action == "assign_course":
            course_code = request.data.get("course_code")
            self.assign_course(teacher, course_code)
        elif action == "assign_class":
            class_code = request.data.get("class_code")
            self.assign_class(teacher, class_code)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_201_CREATED)
        
        

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
      

class WeeklyTimetableView(APIView):
    def get(self, request):
        try:
            class_periods = ClassPeriod.objects.all().prefetch_related(
                'classrooms', 'courses'
            ).order_by('day_of_week', 'start_time')
            
            timetable = {}
            for period in class_periods:
                day = period.day_of_week.strftime("%A")
                if day not in timetable:
                    timetable[day] = []
                
               
                related_objects = ClassPeriodClassPeriod.objects.filter(class_period=period)
                classrooms = [obj.classroom for obj in related_objects]
                courses = [obj.course for obj in related_objects]
                
                timetable[day].append({
                    'start_time': period.start_time.strftime("%H:%M"),
                    'end_time': period.end_time.strftime("%H:%M"),
                    'classrooms': [classroom.name for classroom in classrooms],
                    'courses': [course.course_title for course in courses],
                    'day_of_week': period.day_of_week.strftime("%A")
                })

            return Response(timetable, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)