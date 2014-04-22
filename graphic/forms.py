from django import forms

class UploadCSV(forms.Form):
	file  = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))