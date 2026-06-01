import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

max_attempts = 7
attempts = 0

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100.")
print(f"You have {max_attempts} attempts.\n")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break

    elif guess < secret_number:
        print("Too low! Try again.")

    else:
        print("Too high! Try again.")

    print(f"Attempts left: {max_attempts - attempts}\n")

if guess != secret_number:
    print(f"\n Game Over! The correct number was {secret_number}.")