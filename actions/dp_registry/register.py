# dp_registry/register.py

import os
import json
import requests


class EntraAuth():

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
        GET_URL = 'https://api.ingka.ikea.com/dpr/v1/data_product'
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }
        response = requests.get(GET_URL, headers=headers)
        return response.json()


def main():
    data_product_spec = os.getenv('INPUT_DP_SPEC')

    # Read attributes from data product spec file
    data_product_spec = json.loads(data_product_spec)
    print(f"The data product name is: {data_product_spec['display_name']}")
    print(f"The data product team is: {data_product_spec['team']['name']}")

    # Get data products from DPR
    entra_auth = EntraAuth()
    auth_response = entra_auth.authorisation()
    access_token = auth_response.get("access_token")
    data_products = entra_auth.get_data_products(access_token)
    print (len(data_products))
    print(data_products)

    print(f"The first data product team is: {data_products[0]['team']['name']}")
    print(f"The first data product id is: {data_products[0]['id']}")

if __name__ == "__main__":
    main()
