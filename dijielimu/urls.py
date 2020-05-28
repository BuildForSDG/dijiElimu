from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from course import views

router = routers.DefaultRouter()
router.register(r'course', views.CourseViewSet, basename='Course')
router.register(r'units', views.UnitViewSet, basename='Unit')
router.register(r'videos', views.VideoViewSet, basename='Video')
router.register(r'books', views.BookViewSet, basename='Book')
router.register(r'department', views.DepartmentViewSet, basename='Department')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('users/', include('users.urls')),
    path(r'', include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
