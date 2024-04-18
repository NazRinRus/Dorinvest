from django.urls import path, include
from rest_framework.routers import DefaultRouter

from exhibition.views import exhibition

router = DefaultRouter()

router.register(r'foto', exhibition.FotoExhibitionViewSet, 'foto-exhibition')
#router.register(r'now', exhibition.ExhibitionNowAPIRetrieve.as_view(), 'now-exhibition')

urlpatterns = [
    path('exhibition/', exhibition.ExhibitionAPIList.as_view(), name='exhibitions'),
    path('exhibition/<int:pk>/', exhibition.ExhibitionAPIRetrieve.as_view(), name='exhibition'),
    path('exhibition/now/', exhibition.ExhibitionNowAPIRetrieve.as_view({'get': 'list'}), name='now-exhibition'),
    path('exhibition/previous/', exhibition.ExhibitionPreviousAPIView.as_view({'get': 'list'}), name='prev-exhibition'),
    path('faq/', exhibition.FAQAPIList.as_view(), name='faq'),
    path('feedback/',  exhibition.FeedbackAPIView.as_view({'get': 'list', 'post': 'create'}), name='feedback'),
    path('exhibition/', include(router.urls)),
]
