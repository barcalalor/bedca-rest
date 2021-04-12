from rest_framework import serializers

from core.models import Food, Component


class FoodSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = [
            'id',
        ]


class FoodSerializerDetail(serializers.ModelSerializer):
    components = ""

    class Meta:
        model = Food
        fields = [
            'id',
            'es_description',
            'en_description',
            'group'
        ]


class ComponentSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = [
            'id',
            'es_description',
            'en_description',
            'value',
            'meassure'
        ]


class FoodProfileSerializer(serializers.ModelSerializer):
    components = ComponentSerializerList(many=True)

    class Meta:
        model = Food
        fields = [
            'id',
            'es_description',
            'en_description',
            'group',
            'components'
        ]
