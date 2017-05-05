from rest_framework import serializers

from readerWeb.models import ReadCommend


class ReadCommendSerializer(serializers.ModelSerializer):
    chipId = serializers.CharField()
    token = serializers.CharField()
    status = serializers.IntegerField(allow_null=True, default=0)

    class Meta:
        model = ReadCommend
        fields = ['chipId', 'token', 'status']
