import random
import string


class WeakPasswordError(Exception):
    pass


def generate_password(length=12):
    if length < 8:
        length = 8

    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)

    remaining_length = length - 4
    all_characters = string.ascii_letters + string.digits + string.punctuation
    remaining = [random.choice(all_characters) for _ in range(remaining_length)]

    password_list = list(lowercase + uppercase + digit + special) + remaining
    random.shuffle(password_list)

    return "".join(password_list)


def validate_password(password):
    if len(password) < 8:
        raise WeakPasswordError("Password must be at least 8 characters long.")

    if not any(char.isupper() for char in password):
        raise WeakPasswordError("Password must contain at least one uppercase letter.")

    if not any(char.islower() for char in password):
        raise WeakPasswordError("Password must contain at least one lowercase letter.")

    if not any(char.isdigit() for char in password):
        raise WeakPasswordError("Password must contain at least one digit.")

    if not any(char in string.punctuation for char in password):
        raise WeakPasswordError("Password must contain at least one special character.")

    return True


def main():
    print("=" * 40)
    print("   Password Generator & Validator")
    print("=" * 40)

    while True:
        print("\n1. Generate a strong password")
        print("2. Validate your password")
        print("3. Exit")
        print("-" * 40)

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            try:
                length = int(input("Enter desired password length (minimum 8): "))
                password = generate_password(length)
                print(f"\nGenerated Password : {password}")
            except ValueError:
                print("Invalid length. Please enter a number.")

        elif choice == "2":
            password = input("Enter your password to validate: ").strip()
            try:
                validate_password(password)
                print("Password is strong and valid.")
            except WeakPasswordError as e:
                print(f"Weak password: {e}")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


main()