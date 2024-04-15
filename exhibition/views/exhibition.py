from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from exhibition.serializers.api.exhibition import FotoExhibitionSerializer
from exhibition.models.exhibition import Foto


class FotoExhibitionViewSet(viewsets.ModelViewSet):
    serializer_class = FotoExhibitionSerializer
    queryset = Foto.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = "__all__"
    filterset_fields = [
        "id",
        "foto",
    ]


