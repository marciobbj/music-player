from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from .serializers import TrackSerializer
from .models import Track


class TrackAPIView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = AllowAny,
