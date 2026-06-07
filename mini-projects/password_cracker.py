import itertools
import time

print("=== Brute Force Password Simulator ===")

target = input("Enter a 3 Digit lower case password to check :").strip().lower()

chars = "abcdefghijklmnopqrstuvwxyz"
start_time = time.time()
attempts = 0
cracked = False
print("/nSearching for Match....")

for guess_tuple in itertools.product(chars, repeat=3):
    attempts += 1
    guess = "".join(guess_tuple)

    if guess == target:
        end_time = time.time()
        duration = end_time - start_time
        print("/nPassword Cracked Seccesfully")
        print(f"Attempts :{attempts}")
        print(f"Decrypted Text : {guess}")
        print(f"Duration : {duration:.4f} Second")
        cracked = True
        break

if not cracked:
    print("/n Failed Password Must be Exectly three lowercase Letters")