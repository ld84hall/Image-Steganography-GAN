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



for file in os.listdir("cifar100_png/train"):

	key = secrets.randbits(256).to_bytes(32, "little")
	nonce = secrets.randbits(96).to_bytes(12, "little")
	counter = 0
	start = [0x61707865, 0x3320646e, 0x79622d32, 0x6b206574] + list(struct.unpack("<8I", key)) + [counter] + list(struct.unpack("<3I", nonce))
	start = np.array(start, dtype = np.uint32)

	print("working")
	path = os.path.join("cifar100_png/train", file)
	image = cv2.imread(path)
	height, width = image.shape[:2]
	randnum = random.randint(1,4)
	randnum2 = random.randint(1,2)
	toembed = encryptor.bitstringgen()
	print(len(str(toembed)))

	n = len(str(toembed))
	coords = chacha20v2.randomcoords(chacha20v2.chacha(start,n), height, width)
	print(f"{len(coords)} is the length of coords")
	if randnum2 == 1:
		if randnum == 1:
			stego = randomlsb.encoder(toembed, image, coords)
			name = os.path.splitext(file)[0]
			output = name +".png"
			print(output)
			cv2.imwrite(os.path.join("images/train/stegs", output), stego)
		elif randnum == 2:
			stego = lsbmatching.encoder(toembed, image, coords)
			name = os.path.splitext(file)[0]
			output = name +".png"
			print(output)
			cv2.imwrite(os.path.join("images/train/stegs", output), stego)
		elif randnum == 3:
			stego = textureadaptivelsb.encoder(toembed, image, coords)
			name = os.path.splitext(file)[0]
			output = name +".png"
			print(output)
			cv2.imwrite(os.path.join("images/train/stegs", output), stego)
		else:
			stego = randommultibit.encoder(toembed, image, coords)
			name = os.path.splitext(file)[0]
			output = name +".png"
			print(output)
			cv2.imwrite(os.path.join("images/train/stegs", output), stego)
	else:
		name = os.path.splitext(file)[0]
		output = name +".png"
		print(output)
		cv2.imwrite(os.path.join("images/train/covers", output), image)

print("Done!")



