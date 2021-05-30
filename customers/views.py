from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.template import loader

from customers.models import Customer


# Create your views here.
def index(request):
  return render(request, 'customers/home.html')

def all_customers(request):
  all_customers = get_list_or_404(Customer)
  template_data = {
    'customers_list': all_customers
  }
  return render(request, 'customers/list.html', template_data)

def single_customer(request, customer_id):
  customer = get_object_or_404(Customer, pk=customer_id)
  template_data = {
    'customer': customer
  }
  return render(request, 'customers/detail.html', template_data)
