import string
import secrets
import argparse

def generate_password(length: int, use_upper: bool, use_digits: bool):
    pool = string.ascii_lowercase 
    if use_upper:
        pool += string.ascii_uppercase
    if use_digits:
        pool += string.digits
    chars = []
    if not pool:
        raise ValueError("Character pool is empty, enable at least one option")
    for i in range(length):
        char = secrets.choice(pool)
        chars.append(char)
    password = "".join(chars)
    return password

p = argparse.ArgumentParser()
p.add_argument('--length', type=int, default=12)
p.add_argument('--upper', action='store_true')
p.add_argument('--digits', action='store_true')

args = p.parse_args()
pwd = generate_password(
    length = args.length,
    use_upper = args.upper,
    use_digits = args.digits,
)
print(pwd)