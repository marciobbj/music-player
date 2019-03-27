import json

from rest_framework import mixins
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Track
from .serializers import TrackSerializer


class TrackAPIView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = AllowAny,

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            data=json.dumps(
                {'detail': 'deleted'},
            ), status=status.HTTP_200_OK,
        )
