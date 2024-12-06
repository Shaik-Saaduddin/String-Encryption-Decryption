import sys 
sys.path.insert(1,'C://Users//user//OneDrive//Desktop//Project')
from key_gen import key
from cryptography.fernet import Fernet
from encrypt import  fernet_object, encrypted_text

#import the necessary packages and variables required to decrypt

decrypted_text = fernet_object.decrypt(encrypted_text).decode()
#decrypt the encrypted text using .decode() method
#decrypted text is stored in 'decrypted_text' variable

print('Decrypted text is: ', decrypted_text)