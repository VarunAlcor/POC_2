from rest_framework .filters import SearchFilter
from registration_api.models import *
from django_filters import filters
import django_filters
from django_filters import rest_framework as filters

class CommonCustInfo_filter(filters.FilterSet):
    class Meta:
        model = CommonCustInfo
        fields = '__all__'