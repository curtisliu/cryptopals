import base64
from Crypto.Cipher import AES
from util import decrypt_aes_ecb


def detect_aes_ecb(s):
    BLOCK_SIZE = 16
    chunks = [s[i:i + BLOCK_SIZE] for i in range(0, len(s), BLOCK_SIZE)]
    count_repeats = len(chunks) - len(set(chunks))
    return count_repeats

with open('set1/8.txt', 'r') as f:
  all_lines = []
  for line in f:
    s = bytes.fromhex(line)
    all_lines.append((detect_aes_ecb(s), s))
  print(max(all_lines))
