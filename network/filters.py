import django_filters

from network.models import NetworkNode


class NetworkNodeFilter(django_filters.FilterSet):
    """
    Фильтр для модели узла сети
    """
    country = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = NetworkNode
        fields = ['country']
