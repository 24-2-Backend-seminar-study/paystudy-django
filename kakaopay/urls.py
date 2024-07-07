from django.urls import path
from .views import PayReadyView

app_name = "kakopay"
urlpatterns = [
    # CBV url path
    path("ready/", PayReadyView.as_view()),
]