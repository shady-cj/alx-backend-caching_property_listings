from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from .models import Property
from .serializers import PropertySerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .utils import get_all_properties


@method_decorator(cache_page(60), name="get")
class PropertyListView(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def get_queryset(self):
        return get_all_properties()

