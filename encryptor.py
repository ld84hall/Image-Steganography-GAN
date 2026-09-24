import chacha20v2
import random
import secrets
import struct
import numpy as np
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def bitstringgen():
	indices = []
	indices = np.array(indices)

	file = open("pg1342pride&prejudice.txt")
	text = file.read()
	text = text.split(" ")

	key1 = secrets.randbits(256).to_bytes(32, "little")
	key2 = secrets.randbits(256).to_bytes(32, "little")

	nonce = secrets.randbits(96).to_bytes(12, "little")
	counter = 0
	start = [0x61707865, 0x3320646e, 0x79622d32, 0x6b206574] + list(struct.unpack("<8I", key1)) + [counter] + list(struct.unpack("<3I", nonce))
	start = np.array(start, dtype = np.uint32)

	n = 1
	indices = []
	wordlist = []
	encrypted = b""

	for i in range(n):
		new_list = chacha20v2.chacha(start, i+1).tolist()
		indices += new_list

	for index in indices:
		index = int(index % len(text))
		temp = text[index]
		l = len(text[index].encode("utf-8"))
		if (l%16) == 0:
			wordlist.append(temp)
		else:
			t= 16-(l%16)
			temp += "a"*t
			wordlist.append(temp)

	for word in wordlist:
		iv = secrets.randbits(128).to_bytes(16, "little")
		temp = word.encode("utf-8")
		cipher = Cipher(algorithms.AES(key2), modes.CBC(iv))
		encryptor = cipher.encryptor()
		ct = encryptor.update(temp) + encryptor.finalize()
		encrypted += ct


	file.close()

	bitstring = "".join(f"{b:08b}" for b in encrypted)
	return(bitstring)


