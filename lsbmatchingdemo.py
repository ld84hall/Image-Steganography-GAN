import cv2
import numpy as np
import chacha20v2
import struct
import numpy as np
import secrets
import random


def encoder(string, image, coords):
	sequence = (-1,1)
	h,c,t = 0,0,0
	while t<len(string): 
		b = image[coords[h][0]][coords[h][1]][c]
		if b % 2 != int(string[t]):
			add = random.choice(sequence)
			b = int(b) + add
			if b>=0 and b<256:
				image[coords[h][0]][coords[h][1]][c] = b
			elif b==256:
				image[coords[h][0]][coords[h][1]][c] -=2
			else:
				image[coords[h][0]][coords[h][1]][c] +=1
		c = (c+1)%3
		t +=1
		h +=1
	return image


def decoder(image, coords):
	empty = []
	result = []
	h,t,c= 0,0,0
	while h<len(coords):
		b = image[coords[h][0]][coords[h][1]][c]
		b = b%2
		empty.append(str((b)))
		c = (c+1)%3
		h+=1
	for i in range(0,len(empty),8):
		asc = empty[i:i+8]
		result.append(chr(int("".join(asc), 2)))
	return "".join(result)

			
image = cv2.imread("sample_parrot-image.jpg")
hello = "0110100001100101011011000110110001101111"

key = secrets.randbits(256).to_bytes(32, "little")
nonce = secrets.randbits(96).to_bytes(12, "little")
counter = 0
start = [0x61707865, 0x3320646e, 0x79622d32, 0x6b206574] + list(struct.unpack("<8I", key)) + [counter] + list(struct.unpack("<3I", nonce))
start = np.array(start, dtype = np.uint32)

coords = chacha20v2.randomcoords(chacha20v2.chacha(start,7), 399, 228)


#result = encoder(hello, image, coords)
print(decoder(image, coords))

#cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()



