import os
from cryptography.fernet import Fernet

# Generate a random encryption key
key = Fernet.generate_key()

# Save the encryption key to a file
with open('encryption_key.sniper', 'wb') as f:
    f.write(key)

# Load the encryption key from the file
with open('encryption_key.sniper', 'rb') as f:
    key = f.read()

# Initialize the Fernet cipher with the encryption key
cipher = Fernet(key)

# Read the contents of the text file
with open('license.txt', 'rb') as f:
    plaintext = f.read()

# Encrypt the plaintext using the Fernet cipher
ciphertext = cipher.encrypt(plaintext)

# Write the encrypted data to a file
with open('license.pixel', 'wb') as f:
    f.write(ciphertext)

# Delete the plaintext file
os.remove('license.txt')
