from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
def contato(request):
    return render(request, 'contato.html')
def localizacao(request):
    return render(request, 'localizacao.html')
def sobre(request):
    return render(request, 'sobre.html')

