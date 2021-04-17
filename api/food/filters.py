from django.db.models import Q
import django_filters

from core.models import Food, Component


class FoodFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(method='name_filter')
    group = django_filters.CharFilter(method='group_filter')
    component = django_filters.CharFilter(method='component_filter')

    class Meta:
        model = Food
        fields = ['name', 'group']

    def name_filter(self, queryset, name, value):
        return Food.objects.filter(
            Q(es_description__contains=value) | Q(en_description__contains=value))

    def group_filter(self, queryset, name, value):
        return Food.objects.filter(Q(group__id=value))

    def component_filter(self, queryset, name, value):
        search_model = Component.objects.get(id=value)
        return Food.objects.filter(Q(components__in=search_model))
