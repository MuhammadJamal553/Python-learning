import itertools
import time
# Heading
print("=== Brute Force Password Simulator ===")
# 1. Get user PIN input target
target = input("Enter a 4-Digit PIN to check (0000-9999) :").strip().lower()
# 2. Define the allowed character set
chars = "0123456789"
start_time = time.time()
attempts = 0
cracked = False
print("/nSearching for Match....")
# 3. Generate all possible 3-letter combinations
for guess_tuple in itertools.product(chars, repeat=4):
    attempts += 1
    guess = "".join(guess_tuple)
    # Check if the guess matches the target
    if guess == target:
        end_time = time.time()
        duration = end_time - start_time
        print("/n🔓 PIN Cracked Succesfully")
        print(f"Attempts :{attempts}")
        print(f"Decrypted Text : {guess}")
        print(f"Duration : {duration:.4f} Second")
        cracked = True
        break

if not cracked:
    print("/n Failed Password Must be Exectly three lowercase Letters")