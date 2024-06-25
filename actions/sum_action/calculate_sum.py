# sum-action/calculate_sum.py

import os

def main():
    val_a = int(os.getenv('INPUT_VAL_A'))
    val_b = int(os.getenv('INPUT_VAL_B'))
    total = val_a + val_b
    print(f"The sum of VAL_A and VAL_B is: {total}")

if __name__ == "__main__":
    main()

