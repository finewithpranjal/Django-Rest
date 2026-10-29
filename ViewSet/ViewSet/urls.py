from rest_framework import routers
from django.contrib import admin
from api.views import *
from django.urls import path, include

# Creating router object
router = routers.DefaultRouter()
# Register StudentViewSet with the router   
router.register('studentapi', StudentViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
