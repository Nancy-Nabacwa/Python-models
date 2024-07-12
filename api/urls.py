from django.urls import path
from .views import StudentListView
from .views import TeacherListView
from .views import ClassroomListView
from .views import CourseListView
from .views import ClassPeriodListView

urlpatterns = [
    path("students/", StudentListView.as_view(), name = "student_list_view"),
    path("teachers/", TeacherListView.as_view(), name = "teacher_list_view"),
    path("courses/", CourseListView.as_view(), name = "course_list_view"),
    path("class_model/", ClassroomListView.as_view(), name = "classroom_list_view"),
    path("classPeriod/", ClassPeriodListView.as_view(), name = "classPeriod_list_view"),



]

