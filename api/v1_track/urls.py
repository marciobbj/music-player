from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TrackAPIView

router = DefaultRouter()
router.register('tracks', TrackAPIView, base_name='tracks')

urlpatterns = router.urls