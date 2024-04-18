from rest_framework import serializers

from exhibition.models import exhibition, partner, participant


class FotoExhibitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = exhibition.Foto
        fields = ("foto",)


class FotoParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = participant.Avatar
        fields = ("foto",)


class PartnerExhibitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = partner.Partner
        fields = "__all__"


class ParticipantExhibitionSerializer(serializers.ModelSerializer):
    participant_foto = FotoParticipantSerializer(many=True)

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
            "results"
        )


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = exhibition.FAQ
        fields = (
            "question",
            "answer",
        )


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = exhibition.Feedback
        fields = "__all__"