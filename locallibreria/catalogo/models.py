from django.db import models                  #definir modelos
from django.urls import reverse                #direccionar los modelos a urls
import uuid                                   #permite reconocer los campos claves de una clase

class Cliente(models.Model):

	Nombre_del_cliente = models.CharField(max_length=100)
	rut_del_cliente = models.CharField(max_length=9)
	Fecha_de_Naciemiento = models.DateField('Nacimiento', null=True, blank=True)



			
