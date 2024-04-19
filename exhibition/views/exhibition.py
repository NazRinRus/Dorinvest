from datetime import datetime

from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status
from rest_framework import viewsets, filters, generics, mixins
from rest_framework.response import Response

from exhibition.models.exhibition import Foto, Exhibition, FAQ, Feedback
from exhibition.models.participant import TypeParticipant, Participant
from exhibition.serializers.api.exhibition import FotoExhibitionSerializer, ExhibitionSerializer, FAQSerializer, \
    FeedbackSerializer
from exhibition.service import send_message


#####################
###Exhibition########
#####################
class FotoExhibitionViewSet(viewsets.ModelViewSet):
    """
    API фото выставки.
    """
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
    """
    API для предоставления всех выставок.
    """
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
    """
    API для предоставления выставки по её ID.
    """
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
    """
    API для предоставления ближайшей/текущей выставок.
    """
    serializer_class = ExhibitionSerializer

    def get_queryset(self):
        qs = Exhibition.objects.filter(date_end__gte=datetime.now()).order_by('date_end')[:1]
        return qs


@extend_schema_view(
    get=extend_schema(summary='6 прошедших выставок', tags=['Выставки'])
)
class ExhibitionPreviousAPIView(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    API для предоставления 6 последних выставок.
    """
    serializer_class = ExhibitionSerializer

    def get_queryset(self):
        qs = Exhibition.objects.filter(date_end__lte=datetime.now()).order_by('-date_end')[:6]
        return qs


#####################
###Statistics########
#####################
@extend_schema_view(
    get=extend_schema(summary='Статистика по всем выставкам', tags=['Статистика'])
)
class FoundHomeSummaryAPIView(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    API для статистики.
    Отображается сколько всего участников/питомцев взяли домой.
    Сортировка происходит по видам участников со статусом(is_active) True и в рамках всех выставок.
    """
    serializer_class = ExhibitionSerializer

    def list(self, request, *args, **kwargs):
        qs = {}

        type_ps = TypeParticipant.objects.filter(is_active=True)

        for type_p in type_ps:
            total_found_home = Participant.objects.filter(type_p=type_p, found_home=True).count()
            qs[type_p.name] = total_found_home

        return Response(qs)


@extend_schema_view(
    get=extend_schema(summary='Статистика по конкретной выставке', tags=['Статистика'])
)
class FoundHomeSummaryDetailsAPIView(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    API для статистики.
    Отображается сколько всего участников/питомцев взяли домой.
    Сортировка происходит по видам участников со статусом(is_active) True и в рамках конкретной выставки.
    """
    serializer_class = ExhibitionSerializer

    def list(self, request, *args, **kwargs):
        exhibition_id = kwargs.get('exhibition_id')  # извлекаем exhibition_id из kwargs

        if not exhibition_id:
            return Response({'message': 'Не указан идентификатор выставки'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            exhibition = Exhibition.objects.get(pk=exhibition_id)
        except Exhibition.DoesNotExist:
            return Response({'message': 'Выставка не найдена'}, status=status.HTTP_404_NOT_FOUND)

        qs = {}
        participants = exhibition.participants.filter(type_p__is_active=True)

        for participant in participants:
            total_found_home = Participant.objects.filter(
                type_p=participant.type_p,
                exhibition_participant=exhibition,
                found_home=True,
            ).count()

            qs[participant.type_p.name] = total_found_home

        return Response(qs)


################
###Other########
################
@extend_schema_view(
    get=extend_schema(summary='Часто задаваемые вопросы', tags=['FAQ'])
)
class FAQAPIList(generics.ListAPIView):
    """API FAQ - часто задаваемые вопросы и ответы на инх."""
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
