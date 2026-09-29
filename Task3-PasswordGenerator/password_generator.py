

import random 
import string

print("=" * 40)
print("          PASSWORD GENERATOR ")
print("=" * 40)

length = int(input("Enter the desired password length : "))

characters = string.ascii_letters + string.digits + string.punctuation

# Generate Password
password = ""

for i in range(length):
    password += random.choice(characters)

print("\nYour Secure Password :")
print(password)

print("\nPassword generated successfully!")
print("Keep your password safe and secure.")