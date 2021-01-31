# application1/frontend/api/SatlliteClient.py
import requests


class SatelliteClient:
    @staticmethod
    def add_satellite(json):
        payload = {
            'name': json.name.data,
            'location': json.location.data,
            'healthy': json.healthy.data
        }
        url = 'http://csat-service:5002/api/sat/create'
        response = requests.request("POST", url=url, data=payload)
        return response.json()

    @staticmethod
    def get_satellite(id):
        response = requests.request(method="GET", url='http://csat-service:5002/api/sat/' + id)
        product = response.json()
        return product

    @staticmethod
    def update_satellite_location(id,json):
        payload = {
            'location': json.location
        }
        url = 'http://csat-service:5002/api/sat/location/'+id
        response = requests.request("PUT", url=url, data=payload)
        return response.json()

    @staticmethod
    def update_satellite_healthy(id, json):
        payload = {
            'healthy': json.healthy
        }
        url = 'http://csat-service:5002/api/sat/healthy/' + id
        response = requests.request("PUT", url=url, data=payload)
        return response.json()

    @staticmethod
    def delete_satellite(id):
        url = 'http://csat-service:5002/api/sat/' + id
        response = requests.request("DELETE", url=url)
        return response.json()
    @staticmethod
    def get_products():
        r = requests.get('http://csat-service:5002/api/sats')
        products = r.json()
        return products

