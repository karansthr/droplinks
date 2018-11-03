import hashlib

def hash_password(password):
    return hashlib.sha224(bytes(password)).hexdigest()
