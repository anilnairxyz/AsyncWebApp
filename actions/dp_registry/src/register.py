import os

# get the input and convert it to int
a = os.environ.get("CLIENT_ID")
b = os.environ.get("CLIENT_SECRET")
if a and b:
    try:
        num = int(a) + int(b)
    except Exception:
        exit('ERROR: the INPUT_NUM provided ("{}") is not an integer'.format(a))
else:
    num = 1

# to set output, print to shell in following syntax
print(f"::set-output name=num_squared::{num}")
