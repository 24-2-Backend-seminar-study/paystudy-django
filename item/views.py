from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Item
from .serializers import ItemSerializer

# Create your views here.
class ItemList(APIView):

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        name=request.data.get('name')
        price=request.data.get('price')
        stock=request.data.get('stock')

        if not name or not price or not stock:
            return Response({"detail": "fields missing."}, status=status.HTTP_400_BAD_REQUEST)

        item = Item.objects.create(name=name, price=price, stock=stock)

        serializer = ItemSerializer(item)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
