from rest_framework import serializers

from core.models import ComponentGroup


class ComponentGroupSerializerList(serializers.ModelSerializer):
    components = ""

    class Meta:
        model = ComponentGroup
        fields = [
            'id',
        ]


class ComponentGroupSerializerDetail(serializers.ModelSerializer):
    components = ""

    class Meta:
        model = ComponentGroup
        fields = [
            'id',
            'es_description',
            'en_description',
        ]