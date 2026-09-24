import cv2
import numpy as np
import chacha20v2
import struct
import numpy as np
import secrets
import math


def encoder(string, image, coords):
	if len(string) %3 != 0:
		p = len(string) %3 
		string += "0" * (p+3)
	binary= np.unpackbits(image, axis = -1)
	h,c,t = 0,7,0
	while t<len(string)-3:
		current_bits = "".join((binary[coords[h][0]][coords[h][1]][c-2:c+1]).astype(str))
		if current_bits != string[t:t+3]:
			for i in range(3):
				binary[coords[h][0]][coords[h][1]][c-2+i] = int(string[t+i])
		c = (c+8)%24
		t += 3
		h += 1
	binary  = np.packbits(binary, axis = -1)
	return binary


def decoder(image, coords):
	binary = np.unpackbits(image, axis =-1)
	empty = []
	result = []
	h,t,c= 0,0,7
	while h<len(coords):
		for i in range(3):
			empty.append(str((binary[coords[h][0]][coords[h][1]][c-2+i])))
		c = (c+8)%24
		h+=1
	for i in range(0,len(empty),8):
		asc = empty[i:i+8]
		print(asc)
		result.append(chr(int("".join(asc), 2)))
	return "".join(result)

			
#image = cv2.imread("sample_parrot-image.jpg")
#hello = "0110100001100101011011000110110001101111"

"""
key = secrets.randbits(256).to_bytes(32, "little")
nonce = secrets.randbits(96).to_bytes(12, "little")
counter = 0
start = [0x61707865, 0x3320646e, 0x79622d32, 0x6b206574] + list(struct.unpack("<8I", key)) + [counter] + list(struct.unpack("<3I", nonce))
start = np.array(start, dtype = np.uint32)

coords = chacha20v2.randomcoords(chacha20v2.chacha(start,16), 399, 228)
"""

#result = encoder(hello, image, coords)
#print(decoder(result, coords))








