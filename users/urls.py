from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views as view
urlpatterns = [
    path('accounts/profile', view.profile, name='profile'),
    path('accounts/profile-image-update',
         view.update_profile_image, name='create_profile'),
    path('accounts/users', view.Users.as_view(), name='users'),
    path('accounts/<pk>/info',
         view.UserDetailView.as_view(), name='user-detail'),
     path('forum', view.forum, name="forum"),

]
