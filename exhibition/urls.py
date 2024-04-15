from django.urls import path, include
from rest_framework.routers import DefaultRouter

from exhibition.views import exhibition

router = DefaultRouter()

router.register(r'fotoexhibition', exhibition.FotoExhibitionViewSet, 'foto-exhibition')

urlpatterns = [
    path('exhibitionfoto/', exhibition.FotoExhibitionViewSet.as_view(), name='exhibition-foto'),

    path('exhibition/', include(router.urls)),
]
