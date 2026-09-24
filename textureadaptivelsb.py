import cv2
import numpy as np
import chacha20v2
import struct
import numpy as np
import secrets
import random

def encoder(string, image, coords):
	c, t = 7,0
	image = cv2.GaussianBlur(image, (17,17), 1)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gradx = cv2.Sobel(image, ddepth = cv2.CV_32F, dx =1, dy = 0, ksize=3)
	grady = cv2.Sobel(image, ddepth = cv2.CV_32F, dx = 0, dy = 1, ksize =3)
	grad_mag = np.sqrt(gradx**2 + grady**2)
	scores = []
	
	for i, [y,x] in enumerate(coords):
		scores.append([grad_mag[y][x], i])
	scores = np.array(scores)
	scoresort = scores[np.argsort(scores[:, 0])[::-1]]
	image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
	binary= np.unpackbits(image, axis = -1)

	for [s,i] in scoresort:
		if t>=len(string):
			break

		i = int(i)

		binary[coords[i][0]][coords[i][1]][c] = string[t]

		t +=1
		c = (c+8)%24

	binary  = np.packbits(binary, axis = -1)
	return binary

def decoder(image, coords):
	c, t = 7,0
	nonsobelimage = image.copy()
	binary= np.unpackbits(image, axis = -1)
	

	for i in range(len(coords)):
		for t in range(3):
			binary[coords[i][0]][coords[i][1]][c] = 0
			c = (c+8)%24

	image  = np.packbits(binary,axis = -1)

	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	image = cv2.GaussianBlur(image, (17,17), 1)

	gradx = cv2.Sobel(image, ddepth = cv2.CV_32F, dx =1, dy = 0, ksize=3)
	grady = cv2.Sobel(image, ddepth = cv2.CV_32F, dx = 0, dy = 1, ksize =3)
	grad_mag = np.sqrt(gradx**2 + grady**2)
	scores = []
	empty = []
	result = []

	for i, [y,x] in enumerate(coords):
		scores.append([grad_mag[y][x], i])
	scores = np.array(scores)
	scoresort = scores[np.argsort(scores[:, 0])[::-1]]

	binary= np.unpackbits(nonsobelimage, axis = -1)

	for [s,i] in scoresort:

		i = int(i)
		empty.append(str(binary[coords[i][0]][coords[i][1]][c]))
		c = (c+8)%24
	for i in range(0,len(empty),8):
		asc = empty[i:i+8]
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

coords = chacha20v2.randomcoords(chacha20v2.chacha(start,8), 399, 228)

result = encoder(hello, image, coords)
print(decoder(result, coords))
"""

# major deisgn flaw in that the result is a modified image and sobel may not
#produce the same outcomes...

#but tbf may not need the decoder if Urit is going to learn to decode.




