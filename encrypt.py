import sys
sys.path.insert(1,'C://Users//user//OneDrive//Desktop//Project')
from key_gen import key
from cryptography.fernet import Fernet

#import the necessary packages and the key that we generated

fernet_object = Fernet(key)
#create an object for the Fernet
#this will make working on the generated key easier

plain_text = input('Enter plain text: ')
encrypted_text = fernet_object.encrypt(plain_text.encode())
#The plain text is encrypted and stored in the 'encrypted_text' variable

print('Encrypted text is: ',encrypted_text)