from django.urls import path, include
from rest_framework import routers
from .api import BookViewSet


router = routers.DefaultRouter()
router.register('', BookViewSet, 'bookTest' )
 
urlpatterns = [
      path('', include(router.urls)),
   
]
