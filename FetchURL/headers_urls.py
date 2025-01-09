from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv('ENCRYPTION_KEY').encode()
encrypted_url = b'gAAAAABnf2OwmGsF1NgwyTcqNiSe66440UAFF-U8Sxh1ZycEcfq3xEX0NVWjoODh_nEkZAZ7Dpjo6DIBbNlhZuSzt9NE-oo7keoBU60-xXdx0i80ywqN52P6un8srvCKDhR3k7pluLxv'
cipher_suite = Fernet(key)
BASE_URL = cipher_suite.decrypt(encrypted_url).decode()

print(BASE_URL)