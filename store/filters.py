from .models import Property
from django_filters.rest_framework import FilterSet

class PropertyFilter(FilterSet):
    class Meta:
        model = Property
        fields = {
            'region': ['exact'],
            'city': ['exact'],
            'property_type': ['exact'],
            'price': ['gt', 'lt'],
            'area': ['gt', 'lt'],
            'rooms': ['exact'],
            'floor': ['exact'],
            'condition': ['exact'],
            'seller': ['exact'],
            'documents': ['exact']
        }