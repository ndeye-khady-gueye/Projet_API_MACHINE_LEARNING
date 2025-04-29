from rest_framework import serializers # type: ignore

class SegmentationSerializer(serializers.Serializer):
    age = serializers.FloatField()
    revenu = serializers.FloatField()
    score = serializers.FloatField()