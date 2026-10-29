from django.contrib import admin
from django.urls import path
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentget/', StudentAPI.as_view()),
    path('studentget/<int:pk>', StudentAPI.as_view()),
]