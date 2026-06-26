import random

def number_guessing_game():
    print("=" * 40)
    print("   Welcome to the Number Guessing Game!")
    print("=" * 40)

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print(f"I have picked a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it!")
    print("-" * 40)

    while attempts < max_attempts:
        user_input = input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: ")

        if not user_input.isdigit():
            print("Invalid input. Please enter a valid number!\n")
            continue

        guess = int(user_input)

        if guess < 1 or guess > 100:
            print("Invalid range. Please enter a number between 1 and 100!\n")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low. Try a higher number.\n")
        elif guess > secret_number:
            print("Too high. Try a lower number.\n")
        else:
            print("=" * 40)
            print("Congratulations! You guessed it right!")
            print(f"The number was: {secret_number}")
            print(f"You got it in {attempts} attempt(s)!")
            print("=" * 40)
            return

    print("=" * 40)
    print(f"Game over. You've used all {max_attempts} attempts.")
    print(f"The secret number was: {secret_number}")
    print("=" * 40)


def play_again():
    while True:
        print("\nWould you like to play again?")
        choice = input("Enter 'yes' to play again or 'no' to quit: ").strip().lower()

        if choice == 'yes':
            number_guessing_game()
        elif choice == 'no':
            print("\nThanks for playing! Goodbye!")
            break
        else:
            print("Please enter 'yes' or 'no'.")


number_guessing_game()
play_again()