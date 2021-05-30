import requests
from django.conf import settings


def getGeolocationFromAddress(address: str):
    addressGeoData = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={settings.GOOGLE_MAPS_API_KEY}').json()
    return  {
        'latitude': addressGeoData['results'][0]['geometry']['location']['lat'],
        'longitude': addressGeoData['results'][0]['geometry']['location']['lng']
    } if addressGeoData['status'] == 'OK' else { 'latitude': None, 'longitude': None }
    