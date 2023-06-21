from rest_framework import serializers
from .models import VisitModel

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitModel
        fields = "__all__"
