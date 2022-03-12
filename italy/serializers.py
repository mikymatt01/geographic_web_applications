from rest_framework import serializers
from italy.models import Italy

class ItalySerializer(serializers.ModelSerializer):
    class Meta:
        model = Italy
        fields=('comune', )