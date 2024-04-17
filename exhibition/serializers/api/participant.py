from rest_framework import serializers
from exhibition.models import participant


class FotoParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = participant.Avatar
        fields = ("foto",)


class TypeParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = participant.TypeParticipant
        fields = ("code", "name", "is_active", "sort",)


class BreedParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = participant.TypeParticipant
        fields = ("code", "name", "is_active", "sort",)


class ParticipantSerializer(serializers.ModelSerializer):
    participant_foto = FotoParticipantSerializer(many=True)
    breed = BreedParticipantSerializer()
    type_p = TypeParticipantSerializer()

    class Meta:
        model = participant.Participant
        fields = (
            "name",
            "color",
            "other",
            "avatar_id",
            "participant_foto",
            "found_home",
            "type_p",
            "breed",
        )
