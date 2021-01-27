from util import hamming_distance
from util import single_byte_xor_decrypt
import base64

def normalized_hamming_distance_for_keysize(s, keysize, blocks=3):
  total_distance = 0
  for i in range(0, blocks * keysize, keysize):
    distance = hamming_distance(
      s[i:i + keysize],
      s[i + keysize:i + keysize * 2]
    )
    total_distance += distance
  return total_distance / keysize / blocks

def find_keysize_hamming(s):
  distances = {}
  for i in range(2, 40):
    distances[i] = normalized_hamming_distance_for_keysize(s, i, 10)
  for v, k in sorted((v,k) for k,v in distances.items()):
    yield k, v

def split(s, keysize):
  return [s[i:i + keysize] for i in range(0, len(s), keysize)]

def transpose(blocks):
  transposed = []
  for i in range(0, len(blocks[0])):
    block = bytearray(b'')
    for j in range(0, len(blocks)):
      if i < len(blocks[j]):
        block.append(blocks[j][i])
    transposed.append(bytes(block))
  return transposed

print(hamming_distance(b'this is a test', b'wokka wokka!!!'))


def decrypt_repeating_key_xor(s):
  for keysize, score in list(find_keysize_hamming(s))[:5]:
    print('=== Trying keysize: %s===' % keysize)
    transposed = transpose(split(s, keysize))
    total_score = 0
    key = b''
    blocks = []
    for b in transposed:
      k, score = single_byte_xor_decrypt(b)
      total_score += score
      key += k[0]
      blocks.append(k[1])
    print('Key:', key)
    print('Score:', score / len(transposed))
    print('Decrypted:', b''.join(transpose(blocks)))

with open('set1/6.txt', 'r') as f:
  s = base64.b64decode(f.read())
  decrypt_repeating_key_xor(s)
