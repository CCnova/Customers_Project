from django.shortcuts import get_list_or_404, get_object_or_404, render
from rest_framework import viewsets

from .models import Customer
from .serializers import CustomerSerializer

# def index(request):
#   return render(request, 'customers/home.html')

# def all_customers(request):
#   all_customers = get_list_or_404(Customer)
#   template_data = {
#     'customers_list': all_customers
#   }
#   return render(request, 'customers/list.html', template_data)

# def single_customer(request, customer_id):
#   customer = get_object_or_404(Customer, pk=customer_id)
#   template_data = {
#     'customer': customer
#   }
#   return render(request, 'customers/detail.html', template_data)

class CustomerViewSet(viewsets.ModelViewSet):
  """
    API endpoints that allows Customers to be viewed or edited
  """
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer
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
