from rest_framework import serializers
from exhibition.models import exhibition

class FotoExhibitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = exhibition.Foto
        fields = "__all__"

