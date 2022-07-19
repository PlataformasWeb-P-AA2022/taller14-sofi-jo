from django.db import models

# Create your models here.

class Propietario(models.Model):
    opciones_nacionalidades = (
        ('ecuatoriana','Ecuatoriana'),
        ('peruana','Peruana'),
        ('colombiana','Colombiana'),
        )

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=30, choices=opciones_nacionalidades)

    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
                self.apellido,
                self.edad,
                self.nacionalidad)

class Departamento(models.Model):

    costo_departamento = models.IntegerField('costo departamento')
    num_cuartos = models.IntegerField('numero de cuartos')
    num_banos = models.IntegerField('numero de banos')
    valor = models.IntegerField('valor alicuota')
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE,
            related_name="departamentos")

    def __str__(self):
        return "%s %s %d" % (self.costo_departamento,self.num_cuartos,
                                self.num_banos,self.valor)
 