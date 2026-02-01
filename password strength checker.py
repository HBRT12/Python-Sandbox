import re

password = input("Enter your password to check its strength: ")  # User inputs the password to be checked

def check_password_strength(pw=password):
    length_error = len(pw) < 8
    digit_error = re.search(r"\d", pw) is None  # Check for at least one digit
    uppercase_error = re.search(r"[A-Z]", pw) is None # Check for at least one uppercase letter
    lowercase_error = re.search(r"[a-z]", pw) is None  # Check for at least one lowercase letter
    symbol_error = re.search(r"[ @!#$%^&*()<>?/\\|}{~:]", pw) is None  # Check for at least one special character

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Reporting the results~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    if length_error:
        print("Password must be at least 8 characters long.")
    if digit_error:
        print("Password must include at least one digit.")
    if uppercase_error:
        print("Password must include at least one uppercase letter.")
    if lowercase_error:
        print("Password must include at least one lowercase letter.")
    if symbol_error:
        print("Password must include at least one special character.")

    if not (length_error or digit_error or uppercase_error or lowercase_error or symbol_error):
        print("Password is strong.")  # All criteria met

check_password_strength()