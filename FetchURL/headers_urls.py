from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv('ENCRYPTION_KEY').encode()
encrypted_url = b'gAAAAABmuIzlk-GBIMdFBTFtnnl-3fWhVJijccQxpY3gGLrV1zqffvR6Vusxn4Wa_VSskveWCv27cToTu08D-dvvnzH5cADNqk1LSzl_LQLXOXP0t2Nbw5umoMh_rQZIfl1Y7SX7mB7l'
cipher_suite = Fernet(key)
BASE_URL = cipher_suite.decrypt(encrypted_url).decode()