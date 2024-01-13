import random
import string

def generate_password(length=12):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    all_characters = lowercase_letters + uppercase_letters + digits + special_chars

    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    # Ensure at least one character from each category
    password = (
        random.choice(lowercase_letters) +
        random.choice(uppercase_letters) +
        random.choice(digits) +
        random.choice(special_chars)
    )

    # Fill the rest of the password with random characters
    password += ''.join(random.choice(all_characters) for _ in range(length - 4))

    # Shuffle the password to make the order random
    password_list = list(password)
    random.shuffle(password_list)
    shuffled_password = ''.join(password_list)

    return shuffled_password

# Example usage:
password = generate_password()
print(password)
