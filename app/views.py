from rest_framework.generics import ListAPIView
from .serializers import *
from .models import *

class CategoryListView(ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer