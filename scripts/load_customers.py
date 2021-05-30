import csv

import googlemaps
from customers.models import Customer
from customers.utils.geolocation_utils import getGeolocationFromAddress


def run():
    reader = csv.reader(open('customers/data/customers.csv'))
    Customer.objects.all().delete()
    next(reader)
    for row in reader:
        print(row)
        newCostumer = Customer(first_name=row[1], last_name=row[2], email=row[3], gender=row[4], city=row[5], title=row[6])
        newCostumer.save()
        