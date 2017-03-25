from django import forms
from .models import Doctor
from .models import Procedure

class OrderForm(forms.Form):
	case = forms.IntegerField(label='Case: ')
	doctor = forms.ModelMultipleChoiceField(queryset=Doctor.objects.all(), to_field_name="name")
	patient = forms.CharField(max_length=200)
	procedure = forms.ModelMultipleChoiceField(queryset=Procedure.objects.all(), to_field_name="name")
	description = forms.CharField(max_length=500)
	date_in = forms.DateTimeField('order date in')
	date_out = forms.DateTimeField('order date out')