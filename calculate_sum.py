# calculate_sum.py

import os

def main():
    # Read environment variables
    val_a = int(os.getenv('VAL_A'))
    val_b = int(os.getenv('VAL_B'))
    
    # Calculate the sum
    total = val_a + val_b
    
    # Output the result
    print(f"The sum of VAL_A and VAL_B is: {total}")

if __name__ == "__main__":
    main()

