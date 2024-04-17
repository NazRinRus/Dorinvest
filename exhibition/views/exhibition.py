from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, generics
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.views import APIView

from exhibition.serializers.api.exhibition import FotoExhibitionSerializer, ExhibitionSerializer
from exhibition.models.exhibition import Foto, Exhibition

@extend_schema_view(
    get=extend_schema(summary='Фотографии с выставки', tags=['Выставки'])
)
class FotoExhibitionViewSet(viewsets.ModelViewSet):
    serializer_class = FotoExhibitionSerializer
    queryset = Foto.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = "__all__"
    filterset_fields = [
        "exhibition_id",
    ]


@extend_schema_view(
    get=extend_schema(summary='Информация о выставках', tags=['Выставки'])
)
class ExhibitionAPIList(generics.ListAPIView):
    serializer_class = ExhibitionSerializer
    queryset = Exhibition.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = "__all__"
    filterset_fields = [
        "date_begin",
    ]

@extend_schema_view(
    get=extend_schema(summary='Информация о выставке', tags=['Выставки'])
)
class ExhibitionAPIRetrieve(generics.RetrieveAPIView):
    serializer_class = ExhibitionSerializer
    queryset = Exhibition.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = "__all__"

    def get_queryset(self):
        qs = Exhibition.objects.all().prefetch_related('exhibition_foto')
        return qs