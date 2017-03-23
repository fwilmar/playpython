from django.shortcuts import render


# Create your views here.


from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from django.views import generic
from .models import Order


class IndexView(generic.ListView):
	template_name= 'sheduler/index.html'
	context_object_name = 'latest_order_list'

	def get_queryset(self):
		return Order.objects.order_by('-date_in')[:5]


class DetailView(generic.DetailView):
	model = Order 
	template_name = 'sheduler/detail.html'
