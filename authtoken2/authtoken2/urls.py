from rest_framework import routers
from django.contrib import admin
from api.views import *
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from api.auth import CustomAuthToken # Importing the CustomAuthToken class from api.auth module

# Creating router object
router = routers.DefaultRouter()
# Register StudentViewSet with the router   
router.register('studentapi', StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # Code for login and logout using session authentication (coz session authentication dons't provide built-in login and logout views by default), in Browsable API, you can login and logout using the following urls
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Code for obtaining token for a user using Token Authentication, you can obtain token for a user using the following url
    # path('gettoken/', obtain_auth_token, name='get_token'),  # Endpoint to obtain token for a user

    # Code for obtaining token for a user using Custom Token Authentication, you can obtain token for a user using the following url
    path('customtoken/', CustomAuthToken.as_view(), name='custom_token'),
]
