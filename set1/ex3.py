from util import single_byte_xor_decrypt

b = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
print(single_byte_xor_decrypt(b))