from django.urls import path
from . import views as view

urlpatterns = [
    path('create-course', view.create_course, name='create-course'),
    path('add-videos', view.create_course_video, name='add-video'),
    path('add-documents', view.CourseDocumentsCreate.as_view(), name='add-documents'),
    path('<pk>', view.CourseDetailView.as_view(), name= 'course-detail'),
    path('', view.CourseListView.as_view(), name ='course-list'),
]
