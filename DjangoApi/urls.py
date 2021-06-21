
from django.contrib import admin
from django.urls import path
from api.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    # Normal List, Create, of user's API.
    path('studentInfo/<int:pk>', student_detail),
    # path('studentList/', studentList),
    # path('studentCreate/', studentCreate),
    path('studentApi/', studentApi),
    path('studentApi/<int:pk>', studentApi),
    # class Based APIView
    path('studentAPI/', StudentAPI.as_view()),
    path('studentAPI/<int:pk>', StudentAPI.as_view()),

    # GenericAPIView and Model Mixin
     path('studentList/', StudentList.as_view()),
     path('studentCreate/', StudentCreate.as_view()),






]
