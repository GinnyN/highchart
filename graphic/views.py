from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from csv import DictReader, excel_tab
from graphic import forms, models

# Create your views here.

class Root(TemplateView):
	template_name="upload.html"

	def get_context_data(self, **kwargs):
		context = super(Root, self).get_context_data(**kwargs)
		context["form"] = forms.UploadCSV()
		return context

class Upload(View):
	http_method_names = ["post"]

	def post(self, request, *args, **kwargs):
		form = forms.UploadCSV(request.POST,request.FILES)
		if form.is_valid():
			data = [row for row in DictReader(request.FILES["file"].read().splitlines(), delimiter=";")]
			for row in data:
				try:
					marca = models.Marca.objects.get(marca=row["Marca"])
				except:
					marca = models.Marca(marca=row["Marca"])
					marca.save()

				models.Article(number=row["Articulo"],
					description=unicode(row["Descripcion"], "utf-8", "ignore"),
					vigencia=row["Vigencia"],
					marca=marca,
					stock=row["Stock"]).save()
		return redirect("root")