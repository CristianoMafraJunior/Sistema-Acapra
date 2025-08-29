from django.shortcuts import render
from acapra.models.animal import Animal
<<<<<<< HEAD

def AdocoesAdmin(request):
    query = request.GET.get("q", "")  # pega o termo buscado
    animais = Animal.objects.filter(status_adocao="A") 
    if query:
        animais = animais.filter(nome__icontains=query)

    return render(request, "acapra/admin_adocoes.html", {"animais": animais, "query": query})
=======


def AdocoesAdmin(request):
    animais = Animal.objects.filter(status_adocao="A")  # só adotados
    return render(request, "acapra/admin_adocoes.html", {"animais": animais})
>>>>>>> b452eddd0296e785cd0aa68cdc83b66e4268d177
