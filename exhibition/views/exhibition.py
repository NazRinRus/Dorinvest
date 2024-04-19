from datetime import datetime

from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status
from rest_framework import viewsets, filters, generics, mixins
from rest_framework.response import Response

from exhibition.models.exhibition import Foto, Exhibition, FAQ, Feedback
from exhibition.serializers.api.exhibition import FotoExhibitionSerializer, ExhibitionSerializer, FAQSerializer, \
    FeedbackSerializer
from exhibition.service import send_message


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
        return qs


@extend_schema_view(
    get=extend_schema(summary='6 прошедших выставок', tags=['Выставки'])
)
class ExhibitionPreviousAPIView(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = ExhibitionSerializer

    def get_queryset(self):
        qs = Exhibition.objects.filter(date_end__lte=datetime.now()).order_by('-date_end')[:6]
        return qs


@extend_schema_view(
    get=extend_schema(summary='Часто задаваемые вопросы', tags=['FAQ'])
)
class FAQAPIList(generics.ListAPIView):
    serializer_class = FAQSerializer
    queryset = FAQ.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = "__all__"


@extend_schema_view(
    get=extend_schema(summary='Заявки на приобретение питомца', tags=['Заявки'])
)
class FeedbackAPIView(viewsets.ModelViewSet):
    """API для создания заявки на получение питомца и отправки её на почту."""
    queryset = Feedback.objects.all()  # добавляем queryset
    serializer_class = FeedbackSerializer

    def create(self, request, *args, **kwargs):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            phone = serializer.validated_data.get('phone')
            email = serializer.validated_data.get('email')
            participant = serializer.validated_data.get('participant')

            feedback = Feedback(name=name, phone=phone, participant=participant, email=email)
            feedback.save()
            db = {
                'name': name,
                'phone': phone,
                'participant': participant,
                'email': email,
            }
            send_message(db=db)

            return Response({'message': 'Feedback created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
