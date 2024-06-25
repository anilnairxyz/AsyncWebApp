# sum_action/calculate_sum.py

import yaml
import sys

def main():
    # Read command-line arguments
    val_a = int(sys.argv[1])
    val_b = int(sys.argv[2])
    numbers_file = sys.argv[3]

    # Read numbers from YAML file
    with open(numbers_file, 'r') as file:
        numbers = yaml.safe_load(file)
    
    yaml_number1 = numbers['numbers']['number1']
    yaml_number2 = numbers['numbers']['number2']
    
    # Calculate the sum
    total = val_a + val_b + yaml_number1 + yaml_number2
    
    # Output the result
    print(f"The sum of VAL_A, VAL_B, number1, and number2 is: {total}")

if __name__ == "__main__":
    main()

# import os
# import yaml
# 
# def main():
#     # Read environment variables
#     val_a = int(os.getenv('INPUT_VAL_A'))
#     val_b = int(os.getenv('INPUT_VAL_B'))
#     
#     # Read numbers from YAML file
#     with open('/app/numbers.yaml', 'r') as file:
#         numbers = yaml.safe_load(file)
#     
#     yaml_number1 = numbers['numbers']['number1']
#     yaml_number2 = numbers['numbers']['number2']
#     
#     # Calculate the sum
#     total = val_a + val_b + yaml_number1 + yaml_number2
#     
#     # Output the result
#     print(f"The sum of VAL_A, VAL_B, number1, and number2 is: {total}")

if __name__ == "__main__":
    main()

