from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    ruc=models.IntegerField(max_length=11)
    razon_social=models.CharField(max_length=100)
    direccion=models.CharField(max_length=200)
    def __unicode__(self):
        return U"%s-%s" %(self.ruc,self.razon_social)

class Producto(models.Model):
    codigo=models.CharField(max_length=10)
    nombre=models.CharField(max_length=50)
    precio_unit=models.FloatField()
    afecto=models.BooleanField(default=False)
    stock=models.IntegerField()
    estado=models.BooleanField(default=True)
    igv=models.FloatField()


    def __unicode__(self):
        return U"%s"%self.nombre



class Factura(models.Model):
    serie=models.IntegerField(max_length=3)
    numero=models.CharField(max_length=6, unique=True)
    cliente=models.ForeignKey(Cliente)
    fecha=models.DateField(auto_now_add=True)
    producto=models.ManyToManyField(Producto)
    usuario=models.ForeignKey(User)
    def __unicode__(self):
        return U" %s- %s" %(self.cliente, self.fecha)


