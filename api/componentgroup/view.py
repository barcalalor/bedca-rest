from rest_framework import viewsets

from api.componentgroup import serializers
from core.models import ComponentGroup


class ComponentViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return ComponentGroup.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.ComponentGroupSerializerList
        if self.action == "retrieve":
            return serializers.ComponentGroupSerializerDetail
        return serializers.ComponentGroupSerializerList
