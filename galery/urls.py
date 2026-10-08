from django.urls import path
from galery.views import index, images

urlpatterns = [
    path('', index, name='index'),
    path('image/<int:photo_id>', images, name='image'),
]