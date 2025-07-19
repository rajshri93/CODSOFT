import random
import string

def generate_password(length):
    if length < 8:
        return "Password length should be at least 8 characters."

    # Combine all characters: letters (upper & lower), digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure at least one character of each type
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill the rest with random choices from all characters
    password += random.choices(characters, k=length - 8)

    # Shuffle the resulting list to avoid predictable patterns
    random.shuffle(password)

    # Convert list to string
    return ''.join(password)

# Ask user for desired password length
try:
    length = int(input("Enter the desired password length: "))
    print("Generated password:", generate_password(length))
except ValueError:
    print("Please enter a valid number.")
