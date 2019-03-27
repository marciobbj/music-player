from rest_framework import serializers

from .models import Track

allowed_formats = ['mp3', 'wma', 'wav']


class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Track
        fields = 'id', 'name', 'file',

    def validate_file(self, value):
        checks = [(s in value.name) for s in allowed_formats]
        if not any(checks):
            raise serializers.ValidationError(
                'This field must be supplied with an audio file',
            )
        return value
