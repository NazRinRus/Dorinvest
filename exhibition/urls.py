from django.urls import path, include
from rest_framework.routers import DefaultRouter

from exhibition.views import exhibition

router = DefaultRouter()

router.register(r'foto', exhibition.FotoExhibitionViewSet, 'foto-exhibition')

urlpatterns = [
    path('exhibition/', exhibition.ExhibitionAPIList.as_view(), name='exhibitions'),
    path('exhibition/<int:pk>/', exhibition.ExhibitionAPIRetrieve.as_view(), name='exhibition'),
    path('exhibition/', include(router.urls)),
]
