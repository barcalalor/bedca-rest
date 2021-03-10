from rest_framework import serializers

from core.models import Camera


class CameraSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = [
            'id',
            'name',
            'url',
            'enable'         
        ]


class CameraSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = [
            'id'
        ]


class CameraSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = [
            'id'
        ]


class CameraSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = [ 
            'name',
            'url'
        ]