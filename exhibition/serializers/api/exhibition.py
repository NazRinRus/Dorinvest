from rest_framework import serializers
from exhibition.models import exhibition
from .partner import PartnerSerializer
from .participant import ParticipantSerializer


class FotoExhibitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = exhibition.Foto
        fields = ("foto",)


class ExhibitionSerializer(serializers.ModelSerializer):
    exhibition_foto = FotoExhibitionSerializer(many=True)
    partners = PartnerSerializer(many=True)
    participants = ParticipantSerializer(many=True)

    class Meta:
        model = exhibition.Exhibition
        fields = (
            "name",
            "description",
            "bunner",
            "date_begin",
            "date_end",
            "time_event",
            "location",
            "participants",
            "partners",
            "about",
            "exhibition_foto",
        )


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = exhibition.FAQ
        fields = (
            "question",
            "answer",
        )
