from django.contrib import admin
from django.urls import path, include
from api.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('singer', SingerViewSet, basename='singer')
router.register('song', SongViewSet, basename='song')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

]
