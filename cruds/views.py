from django.shortcuts import render, redirect
from .forms import CrudForm
from .models import Crud

def index(request):
    if request.method == 'POST':
        forms = CrudForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    else:
        cruds = Crud.objects.all()
        form = CrudForm()
        return render(request, 'home.html', { "form": form, "cruds": cruds })
    
def show(request, id):
    crudId = Crud.objects.get(id=id)
    form = CrudForm(crudId)
    return render(request, "detail.html", { "form": form, "crudId": crudId })

def update(request, id):
    crudId = Crud.objects.get(id=id)
    forms = CrudForm(request.POST, instance=crudId)
    if forms.is_valid():
        forms.save()
        return redirect('home')
    else:
        return render(request, "detail.html", { "crudId": crudId })
    
def delete(request, id):
    crudId = Crud.objects.get(id=id)
    crudId.delete()
    return redirect('home')