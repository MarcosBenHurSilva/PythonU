import random
import string

def generate_password(length, include_lowercase, include_uppercase, include_numbers, include_symbols):
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    number_chars = string.digits
    symbol_chars = "!@#$%^&*()_+-="

    allowed_chars = ""
    password = ""

    allowed_chars += lowercase_chars if include_lowercase else ""
    allowed_chars += uppercase_chars if include_uppercase else ""
    allowed_chars += number_chars if include_numbers else ""
    allowed_chars += symbol_chars if include_symbols else ""

    if length <= 0:
        return "(password length must be at least 1)"
    if not allowed_chars:
        return "(At least 1 set of character needs to be selected)"

    for _ in range(length):
        random_index = random.randint(0, len(allowed_chars) - 1)
        password += allowed_chars[random_index]

    return password

password_length = 12
include_lowercase = True
include_uppercase = True
include_numbers = True
include_symbols = True

password = generate_password(
    password_length,
    include_lowercase,
    include_uppercase,
    include_numbers,
    include_symbols
)

print(password)