
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # For media files

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/',  include('students.urls', namespace='students')),
    path('', include('students.urls')),
]
