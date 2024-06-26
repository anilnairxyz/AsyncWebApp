# dp_registry/register.py

import os
import json
import requests


class DataProductRegistration():

    def __init__(self):
        self.CLIENT_ID = os.getenv('INPUT_CLIENT_ID')
        self.CLIENT_SECRET = os.getenv('INPUT_CLIENT_SECRET')
        self.SCOPE = "https://api.prod.ingka.com/.default"
        self.DPR_URL = 'https://api.ingka.ikea.com/dpr/v1/data_product'
        self.AUTH_URL = "https://login.microsoftonline.com/720b637a-655a-40cf-816a-f22f40755c2c/oauth2/v2.0/token"

    def authorisation(self):
        payload = {
            "client_id": self.CLIENT_ID,
            "client_secret": self.CLIENT_SECRET,
            "grant_type": "client_credentials",
            "scope": self.SCOPE,
            "content-type": "application/x-www-form-urlencoded",
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }

        response = requests.post(self.AUTH_URL, headers=headers, data=payload)
        return response.json()

    def get_data_products(self, access_token):
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }
        response = requests.get(self.DPR_URL, headers=headers)
        return response.json()

    def create_data_product(self, access_token, data_product_spec):
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }
        response = requests.post(self.DPR_URL, headers=headers, json=data_product_spec)
        return response.json()


def main():
    data_product_spec = os.getenv('INPUT_DP_SPEC')

    # Read attributes from data product spec file
    data_product_spec = json.loads(data_product_spec)
    print(f"The data product name is: {data_product_spec['display_name']}")
    print(f"The data product team is: {data_product_spec['team']['name']}")

    # Get data products from DPR
    registration = DataProductRegistration()
    auth_response = registration.authorisation()
    access_token = auth_response.get("access_token")
    data_product = registration.create_data_product(access_token, data_product_spec)

    print(f"The first data product team is: {data_product['team']['name']}")
    print(f"The first data product id is: {data_product['data_product_id']}")

if __name__ == "__main__":
    main()
