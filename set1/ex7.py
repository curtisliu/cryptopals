import base64
from Crypto.Cipher import AES
from util import decrypt_aes_ecb

key = b'YELLOW SUBMARINE'
with open('set1/7.txt', 'r') as f:
  s = base64.b64decode(f.read())
  print(decrypt_aes_ecb(s, key))
