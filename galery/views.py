from django.shortcuts import render, get_object_or_404
from galery.models import Photos

def index(request):
    photos = Photos.objects.all()
    return render(request, 'galery/index.html', {"cards": photos})

def images(request, photo_id):
    photo = get_object_or_404(Photos, pk=photo_id)
    return render(request, 'galery/imagem.html', {"photo": photo})

