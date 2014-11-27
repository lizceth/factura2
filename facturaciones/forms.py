from django import forms
from .models import Cliente, Factura, Producto
from django.forms import ModelForm

class ClienteForm(ModelForm):
    class Meta:
        model=Cliente

class ProductoForm(ModelForm):
     class Meta:
         model = Producto

