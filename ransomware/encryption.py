import socket, os, threading, queue, random
from cryptography.fernet import Fernet

def encrypt():
    with open("key.key","wb") as f:
        f.write(Fernet.generate_key(512))