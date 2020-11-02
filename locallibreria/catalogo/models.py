from django.db import models                  #definir modelos
from django.urls import reverse                #direccionar los modelos a urls
import uuid                                   #permite reconocer los campos claves de una clase

class Cliente(models.Model):

	Nombre_del_cliente = models.CharField(max_length=100)
	rut_del_cliente = models.CharField(max_length=9)
	Fecha_de_Naciemiento = models.DateField('Nacimiento', null=True, blank=True)

	def __str__ (self):
		return self.rut_del_cliente

class Peliculas(models.Model):
	titulo = models.CharField(max_length=200)
	genero = models.CharField(max_length=50)

	def __str__(self):
		 return self.titulo
	
	def get_absolute_url(self):
		"""Returns the url to access a detail record for this book."""
		return reverse('book-detail', args=[str(self.titulo)])



			
