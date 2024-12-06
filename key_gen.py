from cryptography.fernet import Fernet

#generates a unique key everytime the program runs.
#this makes the encryption more secure

key = Fernet.generate_key()