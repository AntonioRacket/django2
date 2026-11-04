from django.urls import path
from courses.views import CourseListView  # troque courses pelo nome do seu app

app_name = "courses"

urlpatterns = [
    path("listar/", CourseListView.as_view(), name="course_list"),
]