
from django.urls import path

# rewards/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, SchoolViewSet, DataSubmissionViewSet, ConnectivityImpactViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'schools', SchoolViewSet)
router.register(r'submissions', DataSubmissionViewSet)
router.register(r'connectivity-impacts', ConnectivityImpactViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
