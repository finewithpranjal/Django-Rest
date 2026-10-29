from django.contrib import admin
from django.urls import path
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentget/', StudentList.as_view()),
    path('studentcreate/', StudentCreate.as_view()),
    path('studentupdate/<int:pk>', StudentUpdate.as_view()),
    path('studentretrieve/<int:pk>', StudentRetrieve.as_view()),
    path('studentdelete/<int:pk>', StudentDestroy.as_view()),

    # Combinations
    path('studentlistcreate/', StudentListCreate.as_view()),
    path('studentretrieveupdate/<int:pk>', StudentRetrieveUpdate.as_view()),
    path('studentretrievedestroy/<int:pk>', StudentRetrieveDestroy.as_view()),
    path('studentretrieveupdatedestroy/<int:pk>', StudentRetrieveUpdateDestroy.as_view()),
    
    
]
