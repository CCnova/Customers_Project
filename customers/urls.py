from django.urls import path

from . import views

app_name = 'customers'
urlpatterns = [
  path('', views.index, name='home'),
  path('customers', views.all_customers, name='list'),
  path('customers/<int:customer_id>/', views.single_customer, name='detail'),
]
