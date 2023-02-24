
from django import views
from django.urls import path
from .views import (ProductoList, ProductoDetail, ProductoCreate, ProductoUpdate, ProductoDelete,
                    EntradaInicio, PlatoInicio, PostreInicio, BebidaInicio,
                    Inicio,About,contacto, MenuLogin, MenuLogout, SignUpView, UserUpdate, UserProfile, dummy)

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', Inicio.as_view(), name='inicio'),
    path('about', About.as_view(), name='about'),
    path('contacto/',contacto,name='contacto'),
    path('entrada/inicio/', EntradaInicio.as_view(), name='entrada-inicio'),
    path('plato/inicio/', PlatoInicio.as_view(), name='plato-inicio'),
    path('postre/inicio/', PostreInicio.as_view(), name='postre-inicio'),
    path('bebida/inicio/', BebidaInicio.as_view(), name='bebida-inicio'),
    path('producto/list/', ProductoList.as_view(), name='producto-list'),
    path('producto/<pk>/', ProductoDetail.as_view(), name='producto-detail'),
    path('producto/create',ProductoCreate.as_view(), name='producto-create'),
    path('producto/<pk>/update', ProductoUpdate.as_view(), name='producto-update'),
    path('producto/<pk>/delete', ProductoDelete.as_view(), name='producto-delete'),
    path('login/', MenuLogin.as_view(), name = 'menu-login'),
    path("registro/", SignUpView.as_view(), name="menu-registro"),
    path('logout', MenuLogout.as_view(), name= 'menu-logout'),
    path('dummy', dummy, name="dummy"),
    path("user/<pk>", UserProfile.as_view(), name="user-detail"),
    path("user/<pk>/edit", UserUpdate.as_view(), name="user-update"),

]