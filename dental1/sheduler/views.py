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


def index(request):
	print 'Entro a Index'
	if request.method == 'POST':
		print 'Entro a POST'
		form = OrderForm(request.POST)
		order = Order.objects.create(case=form.case)
		#order.case =   form.case
		order.doctor =  form.doctor
		order.patient =  form.patient
		order.procedure = form.procedure
		order.description = form.description
		order.date_in = form.date_in
		order.date_out = form.date_out
		order.save()
		print 'paso por aca'
		if form.is_valid():
			return HttpResponseRedirect('/thanks/')
	else:
		print 'Entro a GET'
		form = OrderForm()
	print 'Salio'
	return render(request, 'sheduler/formOrder.html', {'form':form})
