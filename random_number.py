import random

number__to_guess=random.randint(1,10)
max_attempts=3

print("Welcome to the Number Guessing Game!")
print(f"Guess the number between 1 and 10.You have{max_attempts} attempts.")

for attempt in range(1,max_attempts+1):
    guess=int(input(f"Attempt{attempt}:Enter your guess:"))
    if guess==number__to_guess:
        print(f"Congratulations! You've guessed the number{number__to_guess} correctly!")
        break
    else:
        print("Incorrect guess.Try again.")
else:
    print(f"Sorry,you've used all your attempts.the correct number was {number__to_guess}")    