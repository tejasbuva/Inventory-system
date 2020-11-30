import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    CHOICES = (
        ('asc', 'Ascending'),
        ('dec', 'Descending')
    )

    ordering = django_filters.ChoiceFilter(label='Ordering', choices=CHOICES, method='filter_by_order')

    class Meta:
        model = Product
        fields = {
            'Tags': ['icontains']
        }

    def filter_by_order(self, queryset, name, value):
        if value == 'asc':
            expression = 'date'
        else:
            expression = '-date'
        return queryset.order_by(expression)
