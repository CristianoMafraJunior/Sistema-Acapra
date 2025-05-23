from django.shortcuts import render, get_object_or_404, redirect
from acapra.models import Animal
from acapra.forms import AnimalForm


def EditarAnimal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)

    if request.method == "POST":
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            return redirect("DashboardAdmin")
    else:
        form = AnimalForm(instance=animal)

    return render(
        request, "acapra/editar_animal.html", {"form": form, "animal": animal}
    )
