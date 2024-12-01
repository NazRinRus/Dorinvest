from django.urls import path, include
from api.spectacular.urls import urlpatterns as doc_urls
from exhibition.urls import urlpatterns as exhibition_urls

app_name = 'api'

urlpatterns = [
    path('auth/', include('djoser.urls.jwt')),
]
urlpatterns += doc_urls
urlpatterns += exhibition_urls