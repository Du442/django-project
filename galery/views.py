from django.shortcuts import render

def index(request):

    data = {
        1: {"name":"Nebulosa de Carina",
            "subtitle":"webbtelescope.org / NASA / James Webb"},
        2: {"name":"Galáxia NGC 1079",
            "subtitle":"nasa.org / NASA / Hubble"}
    }

    return render(request, 'galery/index.html', {"cards": data})

def images(request):
    return render(request, 'galery/imagem.html')

