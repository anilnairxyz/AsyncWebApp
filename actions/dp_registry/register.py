# dp_registry/register.py

import os

def main():
    a = int(os.getenv('INPUT_CLIENT_ID'))
    b = int(os.getenv('INPUT_CLIENT_SECRET'))
    total = a + b
    print(f"The sum of VAL_A and VAL_B is: {total}")

if __name__ == "__main__":
    main()
