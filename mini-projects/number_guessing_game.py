# ==================== NUMBER GUESSING GAME ====================
import random
print("Welcome to Number Guessing Game!")
print("I have Picked a Number between 1 and 100")

# Generate a secret random number between 1 to 100
secret_number= random.randint(1,100)
attempts = 0
max_attempts = 10

while attempts < max_attempts:
    try:
        guess = int(input(f"\n Attempts {attempts}/{max_attempts}. Enter Your Guess:"))
        attempts += 1
        if guess == secret_number:
            print(f"Congratulation You Have Guessed it in {attempts} Attempts")
            break
        elif guess < secret_number:
            print ("📈Your Guess Is Low.Try a Higher Number")
        else:
            print("📉Your Guess Is High.Try a Lower Number")
    except ValueError:
        print("❌Try A Valid Number")
if attempts == max_attempts:
    print(f"\n 💀Game Over! The Number Was {secret_number}.")
print("\nThanks For Playing!")

        