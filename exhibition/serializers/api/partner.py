from rest_framework import serializers
from exhibition.models import partner


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = partner.Partner
        fields = (
            "name",
            "logo",
            "website",
        )
