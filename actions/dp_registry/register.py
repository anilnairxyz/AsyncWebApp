# dp_registry/register.py

import os
import json

def main():
    a = int(os.getenv('INPUT_CLIENT_ID'))
    b = int(os.getenv('INPUT_CLIENT_SECRET'))
    data_product_spec = os.getenv('INPUT_DP_SPEC')
    print ("this is ", data_product_spec, a, b)

    # Read attributes from data product spec file
    numbers = json.load(data_product_spec)

    number1 = numbers['numbers']['number1']
    number2 = numbers['numbers']['number2']

    total = a + b + number1 + number2
    print(f"The sum is: {total}")

if __name__ == "__main__":
    main()
