from rest_framework import serializers

from core.models import Food, Component, ComponentType


class FoodSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = [
            'id', 'es_description', 'group'
        ]


class ComponentGroup(serializers.ModelSerializer):
    class Meta:
        model = ComponentType
        fields = ['id', 'es_description', 'en_description']


class ComponentTypeList(serializers.ModelSerializer):
    group = ComponentGroup()

    class Meta:
        model = ComponentType
        fields = ['id', 'es_description', 'en_description', 'group']


class ComponentTypeDetail(serializers.ModelSerializer):
    class Meta:
        model = ComponentType
        fields = ['id', 'es_description', 'en_description']


class ComponentSerializerList(serializers.ModelSerializer):
    type = ComponentTypeDetail()

    class Meta:
        model = Component
        fields = [
            'id',
            'type',
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


class FoodSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = [
            'id',
            'es_description',
            'en_description',
            'group',
        ]
