# a re-write of the crap version I wrote before.

# will use the actual chacha documentation to implement it
# hopefully it will work this time. 

import secrets
import numpy as np
import struct

key = secrets.randbits(256).to_bytes(32, "little")
nonce = secrets.randbits(96).to_bytes(12, "little")
counter = 0
start = [0x61707865, 0x3320646e, 0x79622d32, 0x6b206574] + list(struct.unpack("<8I", key)) + [counter] + list(struct.unpack("<3I", nonce))
start = np.array(start, dtype = np.uint32)



def quarter_round(a,b,c,d, array):
	array[a] = (int(array[b])+int(array[a])) & 0xffffffff
	array[d] = array[d]^array[a]
	array[d] = ((array[d] << 16) & 0xffffffff) | (array[d] >> (16))

	array[c] = (int(array[c])+int(array[d])) & 0xffffffff
	array[b] = array[b]^array[c]
	array[b] = ((array[b] << 12) & 0xffffffff) | (array[b] >> (20))

	array[a] = (int(array[b])+int(array[a])) & 0xffffffff
	array[d] = array[d]^array[a]
	array[d] = ((array[d] << 8) & 0xffffffff) | (array[d] >> (24))

	array[c] = (int(array[c])+int(array[d])) & 0xffffffff
	array[b] = array[b]^array[c]
	array[b] = ((array[b] << 7) & 0xffffffff) | (array[b] >> (25))



def chacha(array, n):
	biglist = []
	for i in range(n):
		working = array.copy()
		working[12] = i
		initial = working.copy()
		r = 0
		while r<10:
			quarter_round(0,4,8,12,working)
			quarter_round(1,5,9,13,working)
			quarter_round(2,6,10,14,working)
			quarter_round(3,7,11,15,working)

			quarter_round(0,5,10,15,working)
			quarter_round(1,6,11,12,working)
			quarter_round(2,7,8,13,working)
			quarter_round(3,4,9,14,working)
			r +=1
		working = np.array(working, dtype = np.uint32)
		result = working + initial
		biglist = np.append(biglist, result)
	return biglist

def randomcoords(array, height, width):
	empty = []
	for i in range(0,len(array),2):
		y = int(array[i])%height
		x = int(array[i+1])%width
		empty.append([y,x])
	return empty

