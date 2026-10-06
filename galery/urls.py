from django.urls import path
from galery.views import index, images

urlpatterns = [
    path('', index),
    path('image/', images),
]