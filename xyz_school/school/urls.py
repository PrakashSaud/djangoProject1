from django.urls import path
from . import views
urlpatterns = [
    path("grade/list", views.GradeList.as_view(), name="gradelist"),
    path("grade/create", views.GradeCreate.as_view(), name="gradecreate"),
    path("grade/update/<pk>", views.GradeUpdate.as_view(), name="gradeupdate"),
    path("grade/delete/<pk>", views.GradeDelete.as_view(), name="gradedelete"),
    path("student/list", views.GradeList.as_view(), name="gradelist"),
    path("student/create", views.StudentCreate.as_view(), name="studentcreate"),
    path("student/update/<pk>", views.StudentUpdate.as_view(), name="studentupdate"),
    path("student/delete/<pk>", views.StudentDelete.as_view(), name="studentdelete"),

]