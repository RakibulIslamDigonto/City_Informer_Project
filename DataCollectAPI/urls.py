from django.urls import path
from .views import DataCollectAPI

urlpatterns = [
    path('', DataCollectAPI.as_view(), name='dataCollect')


]
