from rest_framework import serializers
from datetime import datetime, timedelta
from .models import SessionData


class SessionDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = SessionData,
        fields = '__all__'


class SessionDataRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = SessionData,
        fields = ('authorization_code', 'client_id')

    def create(self, validated_data):
        validated_data['valid_till'] = datetime.utcnow() + timedelta(hours=24)
        return SessionData.objects.create(**validated_data)
