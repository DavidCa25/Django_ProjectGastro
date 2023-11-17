from django.shortcuts import render
from usuarios.models import Usuario
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm

class CreateView(generic.CreateView):
    model = Usuario
    template_name = "usuarios/usuarios_create.html"
    fields = ['nombre', 'apellido', 'email', 'password', 'tipoUsuario', 'telefono', 'direccion']
    success_url = reverse_lazy("usuarios:usuarios_login")

class LoginView(generic.FormView):
    model = Usuario
    template_name = "usuarios/usuarios_login.html"
    form_class = AuthenticationForm
    fields = ['email', 'password']

    def form_valid(self, form):
        return super().form_valid(form)



