from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', views.TeacherList.as_view(), name='teacher_list'),
    path('filter/', views.LessonFilterView.as_view(), name='lesson_filter')
]