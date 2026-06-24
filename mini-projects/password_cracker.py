import itertools
import hashlib
import string
import time
# Heading
print("=== 🔐 Advanced SHA-256 Password Cracker Simulation ===")
# 1. Get user PIN input target
TARGET_HASH = "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
# 2. Define the allowed character set
chars = string.ascii_lowercase
MAX_LENGTH = 3
print(f"Target Hash to crach {TARGET_HASH}")
print("Searching Combinations Spaces....")

start_time = time.time()
cracked = False
for length in range(1,MAX_LENGTH+1):
    if cracked:
        break
    for guess_tuple in itertools.product(chars,repeat=length):
     guess = "".join(guess_tuple)
     guess_hash = hashlib.sha256(guess.encode('utf-8')).hexdigest()
     if guess_hash == TARGET_HASH:
        duration = time.time() - start_time
        print(f" Success Password Cracked : '{guess}'")
        print(f"Time Taken : '{duration}'")
        cracked = True
        break      
if not cracked:
    print("/n Failed Password Must be Exectly three lowercase Letters")