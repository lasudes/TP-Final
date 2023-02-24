from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, UpdateView
from app_menu.models import Categoria, Producto, Contacto
from app_menu.forms import FormularioContacto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin

class Inicio (TemplateView):
    template_name = 'app_menu/inicio.html'


class About(TemplateView):
    template_name = 'app_menu/about.html'

# se creo la view contacto para el formulario web


def contacto (request):

    if request.method == "POST":

        contacto = FormularioContacto(request.POST)
        
        print(contacto)

        if contacto.is_valid:

            informacion = contacto.cleaned_data
            persona = Contacto( nombre = informacion ['nombre'], apellido = informacion ['apellido'],email = informacion['email'], telefono = informacion['telefono'])
            persona.save()
            return render ( request, "app_menu/exito.html")

    else:
        contacto  = FormularioContacto()
        
    return render (request, "app_menu/contacto.html", {"contacto": contacto})



@login_required
def dummy(request):
    render(request, "")

#Se crea el Login

class MenuLogin(LoginView):
    template_name = 'app_menu/login.html'
    next_page = reverse_lazy("producto-list")



class MenuLogout(LogoutView):
    template_name = 'app_menu/logout.html'



class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'app_menu/registro.html'
    success_url = reverse_lazy('menu-login')
    form_class = UserCreationForm
    success_message = "¡¡Se creo tu perfil satisfactoriamente!!"
  


class UserProfile(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = User
    template_name = "app_menu/user_detail.html"
    
    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])


class UserUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = User
    template_name = "app_menu/user_form.html"
    fields = ["email", "first_name", "last_name", "username"]

    def get_success_url(self):
        return reverse_lazy("user-detail", kwargs={"pk": self.request.user.id})
    
    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])
    


class EntradaInicio(ListView):
    queryset = Producto.objects.filter(tipo=1)  # 1 = entrada
    template_name = "app_menu/inicio_entrada.html"
    context_object_name = "productos"

class PlatoInicio(ListView):
    queryset = Producto.objects.filter(tipo=2)   # 2 = plato
    template_name = "app_menu/inicio_plato.html"
    context_object_name = "productos"

class PostreInicio(ListView):
    queryset = Producto.objects.filter(tipo=3)   # 3 = postre
    template_name = "app_menu/inicio_postre.html"
    context_object_name = "productos"

class BebidaInicio(ListView):
    queryset = Producto.objects.filter(tipo=4)   # 4 = bebida
    template_name = "app_menu/inicio_bebida.html"
    context_object_name = "productos"



class ProductoList(LoginRequiredMixin, ListView):
    queryset = Producto.objects.all()
    template_name = "app_menu/producto_list.html"
    context_object_name = "productos"


class ProductoDetail(LoginRequiredMixin, DetailView):
    model = Producto
    template_name = "app_menu/producto_detail.html"


class ProductoCreate (LoginRequiredMixin, CreateView):
    model = Producto
    fields = ['tipo', 'nombre', 'descripcion', 'precio', 'imagen', 'modificacion']
    template_name = "app_menu/producto_form.html"
    success_url = reverse_lazy("producto-list") 


class ProductoUpdate (LoginRequiredMixin, UpdateView):
    model = Producto
    fields = ['tipo','nombre', 'descripcion', 'precio', 'imagen', 'modificacion']
    success_url = reverse_lazy("producto-list")


class ProductoDelete (LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy("producto-list")







