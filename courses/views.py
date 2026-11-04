from django.shortcuts import render
from django.views.generic import ListView,DetailView
from courses.models import Course  # troque courses pelo nome do seu app


class CourseListView(ListView):
    model = Course
    template_name = "courses/course_list.html"
    context_object_name = "courses"
    paginate_by = 10
# Create your views here.
class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/course_detail.html"
    context_object_name = "course"