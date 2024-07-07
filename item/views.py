from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Item
from account.models import UserProfile
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

class ItemDetailView(APIView):

    def post(self, request):
        user_id=request.data.get('userId')
        item_id=request.data.get('itemId')

        if not user_id or not item_id:
            return Response({"detail": "fields missing."}, status=status.HTTP_400_BAD_REQUEST)
        if UserProfile.objects.get(user_id=user_id).point < Item.objects.get(id=item_id).price:
            return Response({"detail": "not enough point."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            user = UserProfile.objects.filter(user_id=user_id)
            item = Item.objects.filter(id=item_id)

        user.update(point=user.point-item.price)
        item.update(stock=Item.objects.get(id=item_id).stock-1)
        serializer = ItemSerializer(item)

        return Response(serializer.data, status=status.HTTP_200_OK)

        
    
