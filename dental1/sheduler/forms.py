from django import forms

class OrderForm(forms.Form):
	case = forms.IntegerField(label='Case: ')