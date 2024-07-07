from django.urls import path

from .views import ItemList, ItemBuyView

app_name = 'item'
urlpatterns=[
    path("", ItemList.as_view()),
    path("buy/", ItemBuyView.as_view(), name="buy"),
]