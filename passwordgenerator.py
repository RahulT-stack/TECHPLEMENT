import random
import string


def generate_password(length):
    # Define the character sets to use in the password
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure the password contains at least one character from each set
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length with random choices from all character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the list to ensure a random order
    random.shuffle(password)

    # Convert the list to a string and return
    return ''.join(password)


# Example usage
password_length = int(input("Enter Password length : "))  # Specify the desired password length
password = generate_password(password_length)
print("Generated password:", password)
