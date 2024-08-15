from django.urls import path
from .views import StudentListView
from .views import TeacherListView
from .views import ClassroomListView
from .views import CourseListView
from .views import ClassPeriodListView
from .views import StudentDetailView
from .views import TeacherDetailView
from .views import ClassroomDetailView
from .views import CourseDetailView
from .views import ClassPeriodDetailView
from .views import WeeklyTimetableView

urlpatterns = [
    path("students/", StudentListView.as_view(), name = "student_list_view"),
    path("teachers/", TeacherListView.as_view(), name = "teacher_list_view"),
    path("courses/", CourseListView.as_view(), name = "course_list_view"),
    path("class_model/", ClassroomListView.as_view(), name = "classroom_list_view"),
    path("classPeriod/", ClassPeriodListView.as_view(), name = "classPeriod_list_view"),
    path('timetable/', WeeklyTimetableView.as_view(), name='weekly_timetable'),
    path("students/<int:id>/", StudentDetailView.as_view(),name="student_detail_view" ),
    path("teachers/<int:id>/", TeacherDetailView.as_view(),name="teacher_detail_view" ),
    path("classrooms/<int:id>/", ClassroomDetailView.as_view(),name="classroom_detail_view" ),
    path("courses/<int:id>/", CourseDetailView.as_view(),name="course_detail_view" ),
    path("classperiod/<int:id>/", ClassPeriodDetailView.as_view(),name="classperiod_detail_view" ),
]

