import os

from django.http import HttpResponse
from django.shortcuts import render
from myproject.settings import BASE_DIR

from customers.models import Customer


# Create your views here.
def index(request):
  return render(request, 'customers/index.html')

def all_customers(request):
  all_customers = Customer.objects.all()
  return HttpResponse(all_customers)

def single_customer(request, customer_id):
  # customer = Customer.objects.(customer_id)
  return HttpResponse(f'Customer {customer_id} page')
