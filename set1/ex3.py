from util import single_byte_xor_decrypt

b = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
result = single_byte_xor_decrypt(b)
print('Result:', result[0][1])
print('Key:', result[0][0])
print('Score:', result[1])
