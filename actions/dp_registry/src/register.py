import os

# get the input and convert it to int
a = os.environ.get("CLIENT_ID")
b = os.environ.get("CLIENT_SECRET")
num = int(a) + int(b)

# to set output, print to shell in following syntax
print(f"::set-output name=num_squared::{num}")
