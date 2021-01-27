from util import fixed_xor

print(fixed_xor(bytes.fromhex('1c0111001f010100061a024b53535009181c'), bytes.fromhex('686974207468652062756c6c277320657965')).hex())
