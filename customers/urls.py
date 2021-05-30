from django.urls import path

from . import views

urlpatterns = [
  path('', views.index),
  path('all_customers', views.all_customers, name='all customers'),
  path('<int:customer_id>/', views.single_customer, name='single customer'),
]
