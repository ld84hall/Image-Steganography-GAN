import encryptor
import os
import random
import randommultibit
import randomlsb
import lsbmatching
import textureadaptivelsb
import cv2
import secrets
import struct
import numpy as np
import chacha20v2

names = ["greyscaleup.png", "greyscaledown.png","greyscaleleft.png","greyscaleright.png"
,"redup.png", "reddown.png","redleft.png","redright.png",
"greenup.png","greendown.png","greenleft.png","greenright.png",
"blueup.png", "bluedown.png","blueleft.png","blueright.png"]

for i in range(50000):

	name = names[(i%len(names))]
	name = "images7/" + name

	key = secrets.randbits(256).to_bytes(32, "little")
	nonce = secrets.randbits(96).to_bytes(12, "little")
	counter = 0
	start = [0x61707865, 0x3320646e, 0x79622d32, 0x6b206574] + list(struct.unpack("<8I", key)) + [counter] + list(struct.unpack("<3I", nonce))
	start = np.array(start, dtype = np.uint32)

	print("working")
	image = cv2.imread(name)
	height, width = image.shape[:2]
	randnum = random.randint(1,4)
	randnum2 = random.randint(1,2)
	toembed = encryptor.bitstringgen()
	print(toembed[0:10])
	print(len(str(toembed)))

	n = len(str(toembed))
	coords = chacha20v2.randomcoords(chacha20v2.chacha(start,n), height, width)
	print(f"{len(coords)} is the length of coords")
	if randnum2 == 1:
		if randnum == 1:
			stego = randomlsb.encoder(toembed, image, coords)
			name2 = str(i) + ".png"
			print(name2)
			cv2.imwrite(os.path.join("images7/train/stegs", name2), stego)
		elif randnum == 2:
			stego = lsbmatching.encoder(toembed, image, coords)
			name2 = str(i) + ".png"
			print(name2)
			cv2.imwrite(os.path.join("images7/train/stegs", name2), stego)
		elif randnum == 3:
			stego = textureadaptivelsb.encoder(toembed, image, coords)
			name2 = str(i) + ".png"
			print(name2)
			cv2.imwrite(os.path.join("images7/train/stegs", name2), stego)
		else:
			stego = randommultibit.encoder(toembed, image, coords)
			name2 = str(i) + ".png"
			print(name2)
			cv2.imwrite(os.path.join("images7/train/stegs", name2), stego)
	else:
		name2 = str(i) + ".png"
		print(name2)
		cv2.imwrite(os.path.join("images7/train/covers", name2), image)

print("Done!")



