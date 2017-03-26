from django.shortcuts import render


# Create your views here.

import sys
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404
from django.views import generic
from .models import Order
from .forms import OrderForm


def add(request):
	print 'Entro a Index'
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			#return HttpResponseRedirect('/articles/all')
	else:
		print 'Entro a GET'
		form = OrderForm()
	return render(request, 'sheduler/formOrder.html', {'form':form})
