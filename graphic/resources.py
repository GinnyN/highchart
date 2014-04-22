from django.conf.urls import patterns, include, url
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from graphic import models
from django.db.models import Avg


class JugoResource(ModelResource):
	class Meta:
		queryset = models.Marca.objects.all()
		resource_name = 'jugo'
		serializer = Serializer()
	
	def dehydrate(self, bundle):
		articles = models.Article.objects.filter(marca=bundle.obj,vigencia="Vigente")
		stock = 0
		for article in articles:
			stock += article.stock
		if len(articles) != 0:
			bundle.data["avg"] = stock / len(articles)
		return bundle