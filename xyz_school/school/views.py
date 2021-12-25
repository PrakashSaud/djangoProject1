from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import *
from .models import Student, Grade

# FOR CLASS BASED VIEW WE NEED LOGINREQURED MIXIN BUT FOR FUNCTION BASED VIEW WE NEED login_required DECORATOR
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

#CLASS BASED VIEW   
class StudentList(LoginRequiredMixin, ListView):        #LoginRequiredMixin must be the first argument
    model = Student
    template_name = 'school/student_list.html'

class GradeList(LoginRequiredMixin, ListView):
    model = Grade
    template_name = 'school/grade_list.html'

class StudentCreate(LoginRequiredMixin, CreateView):
    model=Student
    template_name = 'school/student_create_form.html'
    # fields = ["first_name", "middle_name", "last_name", "grade", "age", "major"]
    form_class=StudentCreateForm

class GradeCreate(LoginRequiredMixin, CreateView):
    model = Grade
    template_name='school/grade_create_form.html'
    fields = ["name", "total_student", "school"]

class StudentUpdate(LoginRequiredMixin, UpdateView):
    model = Student
    template_name='school/student_update_form.html'
    fields = ["first_name", "middle_name", "last_name", "grade", "age", "major"]

class GradeUpdate(LoginRequiredMixin, UpdateView):
    model = Grade
    template_name = 'school/grade_update_form.html'
    fields = ["name", "total_student", "school"]

class GradeDelete(LoginRequiredMixin, DeleteView):
    model = Grade
    template_name = 'school/grade_delete_form.html'

class StudentDelete(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'school/student_delete_form.html'


