from rest_framework import routers
from django.contrib import admin
from api.views import *
from django.urls import path, include

# Creating router object
router = routers.DefaultRouter()
# Register StudentViewSet with the router   
router.register('studentapi', StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # Code for login and logout using session authentication (coz session authentication dons't provide built-in login and logout views by default), in Browsable API, you can login and logout using the following urls
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
