from django_filters import FilterSet

from core.models import Food


class BookFilter(FilterSet):
    class Meta():
        model = Food
        fields = ['es_description', 'en_description', 'group']