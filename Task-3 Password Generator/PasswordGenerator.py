"""
Project 3: Random Password Generator

Goal:
Generate a random password based on the length entered by the user.

Features:
- User chooses password length
- Optional symbols
- Uses letters and numbers
- Input validation
- Generates a secure random password

Author: Ayush Bodade
"""

import random
import string


# Function to generate password
def generate_password(length, use_letters=True, use_numbers=True, use_symbols=False):
    character_pool = ""

    if use_letters:
        character_pool += string.ascii_letters

    if use_numbers:
        character_pool += string.digits

    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        return None

    password = "".join(random.choice(character_pool) for _ in range(length))
    return password


# Main Program
def main():
    print("=" * 40)
    print("     RANDOM PASSWORD GENERATOR")
    print("=" * 40)

    # Get password length
    while True:
        try:
            length = int(input("Enter password length: "))

            if length <= 0:
                print("\n⚠️ Password length must be greater than 0.\n")
                continue

            break

        except ValueError:
            print("\n❌ Please enter a valid number.\n")

    # Ask whether to include symbols
    include_symbols = input("Include symbols? (y/n): ").strip().lower()
    use_symbols = include_symbols == "y"

    # Generate password
    password = generate_password(
        length,
        use_letters=True,
        use_numbers=True,
        use_symbols=use_symbols
    )

    print("\n" + "=" * 40)
    print("        GENERATED PASSWORD")
    print("=" * 40)
    print(password)

    print("\n✅ Password generated successfully!")
    print("Thank you for using Password Generator! 🚀")


# Run the program
if __name__ == "__main__":
    main()