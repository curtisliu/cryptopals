from util import single_byte_xor_decrypt

def detect_single_byte_xor(strings):
  all = []
  for s in strings:
    k, v = single_byte_xor_decrypt(bytes.fromhex(s))
    all.append((v, k))
  return sorted(all)

with open('set1/4.txt', 'r') as f:
  results = detect_single_byte_xor(f.readlines())
  print('Result:', results[0][1][1])
  print('Key:', results[0][1][0])
  print('Score:', results[0][0])
