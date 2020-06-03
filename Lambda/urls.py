from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from school.views import home


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('', home, name='home'),
    path('schools/', include('school.urls')),
    path('books/', include('books.urls')),
    path('', include('users.urls')),
    path('courses/', include('course.urls')),
    path('videos/', include('tutorials.urls')),
    path('posts/', include('posts.urls')),
    path('front/', include('frontend.urls')),
    path('booktest/', include('bookTest.urls')),
    path('admin/', admin.site.urls),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
