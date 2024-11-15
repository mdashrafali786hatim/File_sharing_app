from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_url(user_id):
    return cipher_suite.encrypt(f"user:{user_id}".encode()).decode()

def generate_download_link(filename):
    return cipher_suite.encrypt(filename.encode()).decode()
