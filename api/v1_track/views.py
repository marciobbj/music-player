from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Track
from .serializers import TrackSerializer


class TrackAPIView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = AllowAny,
