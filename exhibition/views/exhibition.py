from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, generics, mixins
from drf_spectacular.utils import extend_schema_view, extend_schema
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from exhibition.serializers.api.exhibition import FotoExhibitionSerializer, ExhibitionSerializer, FAQSerializer
from exhibition.models.exhibition import Foto, Exhibition, FAQ


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

    # def get_queryset(self):
    #     qs = Exhibition.objects.all().prefetch_related('exhibition_foto')
    #     return qs


@extend_schema_view(
    get=extend_schema(summary='Ближайшая или текущая выставка', tags=['Выставки'])
)
class ExhibitionNowAPIRetrieve(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = ExhibitionSerializer

    def get_queryset(self):
        qs = Exhibition.objects.filter(date_end__gte=datetime.now()).order_by('date_end')[:1]
        print(qs)
        return qs


@extend_schema_view(
    get=extend_schema(summary='6 прошедших выставок', tags=['Выставки'])
)
class ExhibitionPreviousAPIView(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = ExhibitionSerializer

    def get_queryset(self):
        qs = Exhibition.objects.filter(date_end__lte=datetime.now()).order_by('-date_end')[:6]
        print(qs)
        return qs


@extend_schema_view(
    get=extend_schema(summary='Часто задаваемые вопросы', tags=['FAQ'])
)
class FAQAPIList(generics.ListAPIView):
    serializer_class = FAQSerializer
    queryset = FAQ.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = "__all__"
