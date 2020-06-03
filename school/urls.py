from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from school import views

app_name = 'school'
urlpatterns = [

    path('create', views.get_school, name='create'),
    path('', views.schools, name='schools'),
    path('<int:pk>', views.SchoolDetailView.as_view(), name='details'),
    path('<int:pk>/students', views.SchooolStudents.as_view(), name='students'),
    path('student/add-student', views.student_add, name='add_student'),
    path('students/<int:pk>/student-detail',
         views.StudentDetail.as_view(), name="student-detail"),
    path('<int:pk>/teachers', views.SchooolTeachers.as_view(), name='teachers'),

    path('teachers/<int:pk>/teacher-detail',
         views.TeacherDetail.as_view(), name="teacher-detail"),
    path('teachers/add-teacher', views.teacher_add, name='add_teacher'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
