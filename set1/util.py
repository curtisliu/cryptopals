import base64
import math
from Crypto.Cipher import AES

# Set 1.1
def hex2base64(s):
  b = bytes.fromhex(s)
  return base64.b64encode(b)

# Set 1.2
def fixed_xor(a, b):
  return bytes(x ^ y for (x, y) in zip(a, b))

# Set 1.3

def normalize_frequencies(frequencies):
  normalized = {}
  total = sum(frequencies.values())
  for k, v in frequencies.items():
    normalized[k] = v / total
  return normalized

def sum_of_squares(a, b):
  total = 0
  for k, v in a.items():
    total += (b.get(k, 0) - a[k]) ** 2
  return total

ENGLISH_LETTER_FREQUENCIES = normalize_frequencies({
' ': 72327800,
'E': 37047647,
'T': 27083970,
'A': 23944887,
'O': 22536157,
'I': 20133224,
'N': 20088720,
'H': 18774883,
'S': 18415648,
'R': 17103717,
'D': 13580739,
'L': 12350767,
'U': 8682289,
'M': 7496355,
'C': 7248810,
'W': 7022120,
'G': 6396495,
'F': 6262477,
'Y': 6005496,
'P': 5065887,
',': 4784859,
'.': 4680323,
'B': 4594147,
'K': 2853307,
'V': 2745322,
'"': 2566376,
'\'': 1699273,
'-': 1000071,
'?': 469889,
'X': 454572,
'J': 448397,
';': 311385,
'!': 300580,
'Q': 275136,
'Z': 268771,
':': 96752,
'1': 63148,
'—': 57781,
'0': 40105,
')': 38729,
'*': 38475,
'(': 38220,
'2': 36981,
'’': 36692,
'`': 36256,
'“': 31829,
'”': 30629,
'3': 25790,
'9': 24985,
'5': 21865,
'4': 21181,
'8': 18853,
'7': 17124,
'6': 17007,
'/': 16757,
'_': 11605,
'[': 11568,
'»': 11551,
']': 11535,
'«': 11187,
'=': 9899,
'´': 8807,
'\xA0': 5326,
'>': 4507,
'~': 4067,
'<': 3995,
'#': 3170,
'·': 2793,
'‘': 2760,
'&': 2690,
'{': 2258,
'}': 2142,
'•': 2055,
'^': 1712,
'|': 1512,
'\\': 1366,
'@': 1354,
'%': 1165,
'$': 1050,
'Ñ': 1005,
})
ENGLISH_LETTERS = ENGLISH_LETTER_FREQUENCIES.keys()

def score(s):
  frequencies = {}
  invalid_chars = 0
  for i in s:
    char = chr(i)
    if char.upper() not in ENGLISH_LETTERS:
      char = 'unknown'
    else:
      char = char.upper()
    if char not in frequencies:
      frequencies[char] = 0
    frequencies[char] += 1
  return invalid_chars + sum_of_squares(normalize_frequencies(frequencies), ENGLISH_LETTER_FREQUENCIES)

def single_byte_xor_decrypt(s):
  results = {}
  for i in range(0, 256):
    xor = fixed_xor(s, bytes([i]) * len(s))
    results[(bytes([i]), xor)] = score(xor)
  # for k, v in sorted((v, k) for k, v in results.items())[:10]:
  #   print(k, v)
  min_key = min(results, key=results.get)
  return min_key, results[min_key]

# Set 1.5
def repeating_key_xor(s, key):
  repeating_key = key * (math.ceil(len(s) / len(key)))
  repeating_key = repeating_key[:len(s)]
  print(s, len(s))
  print(repeating_key, len(repeating_key))
  return fixed_xor(s, repeating_key)

# Set 1.6
def hamming_distance(a, b):
  return sum(bin(x).count('1') for x in fixed_xor(a, b))

# Set 1.7
def decrypt_aes_ecb(s, key):
  aes = AES.new(key, AES.MODE_ECB)
  return aes.decrypt(s)
