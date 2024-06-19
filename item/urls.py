from django.urls import path

from .views import ItemList

app_name = 'item'
urlpatterns=[
    path("", ItemList.as_view()),
]