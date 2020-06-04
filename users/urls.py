from rest_framework.routers import DefaultRouter
from .views import UserViewSet, StudentViewSet, TutorViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'students', StudentViewSet, basename='students')
router.register(r'tutors', TutorViewSet, basename='tutors')
urlpatterns = router.urls
