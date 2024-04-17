from rest_framework import serializers
from exhibition.models import exhibition

class FotoExhibitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = exhibition.Foto
        fields = ("foto",)


class ExhibitionSerializer(serializers.ModelSerializer):
    exhibition_foto = FotoExhibitionSerializer(many=True)
    class Meta:
        model = exhibition.Exhibition
        fields = (
            "name",
            "bunner",
            "date_begin",
            "date_end",
            "location",
            "participants",
            "partners",
            "exhibition_foto",
        )