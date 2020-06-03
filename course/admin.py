from embed_video.admin import AdminVideoMixin
from django.contrib import admin

from .models import (
    Course, CourseVideo, CourseDocument,
)


admin.site.register([Course, CourseVideo, CourseDocument
                   ])
