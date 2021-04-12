from rest_framework import serializers

from core.models import FoodGroup


class FoodGroupSerializerList(serializers.ModelSerializer):
    components = ""

    class Meta:
        model = FoodGroup
        fields = [
            'id',
        ]


class FoodGroupSerializerDetail(serializers.ModelSerializer):
    components = ""

    class Meta:
        model = FoodGroup
        fields = [
            'id',
            'es_description',
            'en_description',
        ]