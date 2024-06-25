# sum_action/calculate_sum.py

import yaml
import sys

import os
import yaml

def main():
    # Read environment variables
    val_a = int(os.getenv('INPUT_VAL_A'))
    val_b = int(os.getenv('INPUT_VAL_B'))
    
    # Read numbers from YAML file
    
    print (type(os.getenv('INPUT_NUMBERS_FILE')))
    # Calculate the sum
    total = val_a + val_b
    
    # Output the result
    print(f"The sum of VAL_A, VAL_B, number1, and number2 is: {total}")

if __name__ == "__main__":
    main()

