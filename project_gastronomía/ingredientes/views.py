from django.shortcuts import render
from ingredientes.models import Ingredientes
from django.views import generic
from django.urls import reverse_lazy, reverse


class indexView(generic.ListView):
    template_name = "ingredientes/ingrediente_list.html"
    context_object_name = "ingrediente_list"

    def get_queryset(self):
        return Ingredientes.objects.all()

class detailView(generic.DetailView):
    model = Ingredientes
    template_name = "mynotes/note_detail.html"

class CreateView(generic.CreateView):
    model = Ingredientes
    template_name = "ingredientes/note_create.html"
    fields = ['name', 'description', 'región', 'image']
    success_url = reverse_lazy('ingredientes:ingrediente_list')

    
class UpdateView(generic.UpdateView):
    model = Ingredientes
    template_name = "ingredientes/Ingrediente_create.html"
    fields = ['title', 'content'] 
    success_url = reverse_lazy('ingredientes:ingrediente_list')

class DeleteView(generic.DeleteView):
    model = Ingredientes
    success_url = reverse_lazy('ingredientes:ingrediente_list')

    def get(model, request, *args, **kwargs):
        return model.delete(request, *args, **kwargs)