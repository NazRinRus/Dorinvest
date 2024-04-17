from rest_framework import serializers
from exhibition.models import exhibition, partner, participant

class FotoExhibitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = exhibition.Foto
        fields = ("foto",)

class PartnerExhibitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = partner.Partner
        fields = "__all__"

class ParticipantExhibitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = participant.Participant
        fields = "__all__"


class ExhibitionSerializer(serializers.ModelSerializer):
    exhibition_foto = FotoExhibitionSerializer(many=True)
    partners = PartnerExhibitionSerializer(many=True)
    participants = ParticipantExhibitionSerializer(many=True)
    class Meta:
        model = exhibition.Exhibition
        fields = (
            "id",
            "name",
            "bunner",
            "date_begin",
            "date_end",
            "location",
            "participants",
            "partners",
            "exhibition_foto",
        )