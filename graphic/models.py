from django.db import models

class Article(models.Model):
	number = models.IntegerField(default=0)
	description = models.CharField(max_length=100,default="Jugo") 
	vigencia = models.CharField(max_length=100,choices=(('Vigente','Vigente'),('Caducado','Caducado')),default="Vigente")
	stock = models.IntegerField(default=0)
	marca = models.ForeignKey("Marca")
class Marca(models.Model):
	marca = models.CharField(max_length=100,default="Marca")