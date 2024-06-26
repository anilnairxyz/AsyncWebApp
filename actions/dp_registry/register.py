# dp_registry/register.py

import os
import json

def main():
    a = int(os.getenv('INPUT_CLIENT_ID'))
    b = int(os.getenv('INPUT_CLIENT_SECRET'))
    data_product_spec = os.getenv('INPUT_DP_SPEC')

    # Read attributes from data product spec file
    data_product_spec = json.loads(data_product_spec)

    print(f"The data product name is: {data_product_spec["display_name"]}")

if __name__ == "__main__":
    main()
