from django.shortcuts import render


# Create your views here.


from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from .models import Order


def detail(request, order_id):
	order = get_object_or_404(Order,pk=order_id)

	#try:
	# 	order = Order.objects.get(pk=order_id)
	# except Order.DoesNotExist:
	# 	raise Http404("La orden no existe")
	#return render("You're looking at order %s" % order_id)
	return render(request, 'sheduler/detail.html', {'order':order})

def results(request, order_id):
	response = "You're looking at the results of order %s"
	return HttpResponse(response % order_id)

	
def index(request):
	latest_order_list = Order.objects.order_by('-date_in')[:5]
	#template = loader.get_template('sheduler/index.html')
	context = {'latest_order_list': latest_order_list}
	#output= ','.join([q.description for q in latest_order_list])
	return render(request, 'sheduler/index.html', context)
	#return HttpResponse(template.render(context, request))
