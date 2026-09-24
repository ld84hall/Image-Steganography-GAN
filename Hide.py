# also featuring Urit

import torch
import random
from torch import nn
from PIL import Image
import torchvision.transforms as transforms
from torchvision.utils import save_image

message_bank_strings = [
    "01011001110001100010100110000001111101110101",
    "11110001101110111000101010110100111000100111",
    "11000100101010111011100100100011011101001100",
    "10111110010101010100111000000100101001110111",
    "10001100111111011001011101101011010110110111",
    "10111000011010101100110110011011100100010011",
    "10100110011100111010000000010011000110101100",
    "10101011010101010001101111010001001010100001",
    "00001101000010001100011000111100000010001111",
    "01011101010101100100011110101000100001001011",
    "01101001111000001110010100010001101100011001",
    "11001101010100000010111000101000000111101100",
    "00001111110000010101111110001001110000100101",
    "11111100000100001000101011100111101101110001",
    "11011000010110101110100000111100010111010110",
    "01001000011110100111111010001110011101110010",
    "01010100111111111011011000011101001010110010",
    "01101001100100101000101000010001100000100101",
    "10111100001100000100100110010111100000011100",
    "11011010011011101111001110001111100001010011",
    "10111100100011101110001010100000111011110001",
    "10101111000011001010000001110110000011110110",
    "00010101001011000110110111111101100010111001",
    "00000101011000000011101101101010100111001001",
    "00001010001000011001100101010010000000110000",
    "11100100101011101100000110001000110100101111",
    "00101111000110010110111100100110101000011011",
    "10001110101101000010101011011001001101110010",
    "00110100100000000001110110010110000101010111",
    "10001100100111011001011000000011100011100111",
    "11111000101000100011101010111100010100010011",
    "11100011000111011001011111000110101101111111",
    "00101101100011010010101010000000000010011101",
    "00100100001011100000010001011111001100110111",
    "01001011111010011111111011101100001101011001",
    "01010101000011011100110110000100010110100001",
    "11111110011001101110001101111110010010000000",
    "10000000010010001100111100011101110110111001",
    "00101101111111111110000101101101011011010100",
    "10100011010011101010101110100111101001010010",
    "10011000111001111011110111001111011101101000",
    "01000000101100110000010010010110001111001000",
    "10001110111110101111101111100010000110111110",
    "11101000000010101101011010111101010010011100",
    "01000111001010110100100100110000101101011001",
    "01010011000101010100100111011101001001001110",
    "00001000000100010001010010011100011100101000",
    "00011100110011000110100100110101000101000010",
    "10001011000000000010010101000011100010100111",
    "10001110111001111100000110000110101011011100",
    "10011011101100110011111111100000010011111111",
    "00000100011100011011100101010101001100111011",
    "11000000101100100110101000001000100010011100",
    "10011011001110001100100001011010111101001101",
    "10111011000010001010101000010001111101111110",
    "01001101100000011001101010100000011100111011",
    "01110001111111000001011100111001111110010001",
    "11000111000011000000101010110101011101100101",
    "10111101101101100101101000000101000100101101",
    "01111110110001000011101110110100111000010011",
    "11101011000110111001101011101001100010010000",
    "10011011100100010000101000101100011001011000",
    "01100001000011000001010100110011101110011010",
    "01111110010100100010110101110010111100110110",
    "11010101000100101001111000101110010111011111",
    "10111000111110110101110101001111000001111111",
    "00100011111101100111100101111010000100001101",
    "00011000110011100000011001000001000010010111",
    "00001011011000001101101111000010010011001100",
    "11100111000111000111101110000000011101110010",
    "01111111111111110100001011010101111101100101",
    "11110000000001100001010100001110111110110011",
    "10001010100011001011111101000010110000111111",
    "10011100100011000000111110100001001111000010",
    "11010110101001100011010111100110101010011011",
    "01000101010101100010001101111000001111001011",
    "00010000011100110010110010100010111011000100",
    "01111010000011110111100011111010010011001000",
    "00010101000100101000000111011001100001010101",
    "10110001101010110011111011100011011001001111",
    "01010100000110111111101111101101100001111010",
    "10001101101111001101100111011111000101000000",
    "01101101001110111110101001100000100011110001",
    "00010111100111100000111011111110000011011100",
    "01100100100000011111101100101110001010110010",
    "10111011011110110101000110110001010101110111",
    "11000000001010000001111011010110001110000100",
    "00010101010111001100001001011000101111101001",
    "01011000100111000110010011001000101110010101",
    "10101001010011000110000001101011110011011011",
    "11110110011010111010000110100000010110010010",
    "10111001111100010010111010111001111111101111",
    "01010000100011111010000110001000001100110110",
    "00101000101101100101110110100010000000101000",
    "11000000011100001101001111010011111001110011",
    "01111110100001010010001101000011010110101010",
    "10011101100101000011010101111000110111100001",
    "01110000101010111001001100010010000011110000",
    "10101101111001100000000001100010000000110110",
    "00001001010111100110010000100111100100110010"
]


class ConvBNReLU(nn.Module):
	def __init__(self, in_channels, out_channels):
		super().__init__()
		self.convolution = nn.Sequential(

			nn.Conv2d(in_channels, out_channels , kernel_size = 3, padding = 1),
			nn.BatchNorm2d(out_channels),
			nn.ReLU()

			)

	def forward(self,x):
		return self.convolution(x)

class Encoder(nn.Module):
	def __init__(self, 
		image_channels = 3, 
		message_length = 44, 
		encoder_feature_depth  = 64,
		pre_message_convs =1,
		post_message_convs =1
		):

		super().__init__()

		self.image_channels = image_channels
		self.message_length = message_length
		self.encoder_feature_depth = encoder_feature_depth 


		self.image_features = nn.Sequential(

			ConvBNReLU(image_channels, encoder_feature_depth),
			ConvBNReLU(encoder_feature_depth, encoder_feature_depth),
			ConvBNReLU(encoder_feature_depth, encoder_feature_depth)

			)

		self.post_message_convolution = nn.Sequential(
			
			ConvBNReLU(encoder_feature_depth + message_length, encoder_feature_depth),
			ConvBNReLU(encoder_feature_depth, encoder_feature_depth),
			ConvBNReLU(encoder_feature_depth, encoder_feature_depth)

		)
		
		self.final_conv = nn.Conv2d(

			in_channels = self.encoder_feature_depth +3,
			out_channels= 3,
			kernel_size = 1

			)

	def message_to_map(self, message):
		array = []
		string = str(message)
		for letter in string:
			if letter == "0":
				new_array = torch.zeros(32,32)
				array.append(new_array)
			else:
				new_array = torch.ones(32,32)
				array.append(new_array)
		return torch.stack(array).unsqueeze(0)

	def forward(self, image, message):
		original_image = image
		processedimg = self.image_features(image)
		processedmsg = self.message_to_map(message)
		imageplusmessage = torch.cat([processedmsg, processedimg], dim=1)
		preresult = self.post_message_convolution(imageplusmessage)
		preresultplusid = torch.cat([preresult, original_image], dim=1)
		return self.final_conv(preresultplusid)


hide = Encoder()

class decoder(nn.Module):
	def __init__(self):
		super().__init__()
		self.stack = nn.Sequential(

			nn.Conv2d(in_channels = 3, out_channels = 64, kernel_size = 3, padding = 1),
			nn.BatchNorm2d(64),
			nn.ReLU(),

			nn.Conv2d(in_channels = 64, out_channels = 64, kernel_size = 3, padding = 1),
			nn.BatchNorm2d(64),
			nn.ReLU(),
			nn.AvgPool2d(kernel_size = 2, stride =2),

			nn.Conv2d(in_channels = 64, out_channels = 128, kernel_size = 3, padding = 1),
			nn.BatchNorm2d(128),
			nn.ReLU(),
			nn.AvgPool2d(kernel_size = 2, stride =2),
			
			nn.Conv2d(in_channels = 128, out_channels = 256, kernel_size = 3, padding = 1),
			nn.BatchNorm2d(256),
			nn.ReLU(),
			nn.AvgPool2d(kernel_size =2, stride = 2),

			nn.AdaptiveAvgPool2d((4, 4)),

			nn.Flatten(),

			nn.Linear(256*4*4, 256),
			nn.ReLU(),
			nn.Dropout(p=0.2),

			nn.Linear(256,44)
			)

	def forward(self, x):
		logits = self.stack(x)
		return logits

urit = decoder()


class Seek(nn.Module):
	def __init__(self):
		super().__init__()
		self.stack = nn.Sequential(

			nn.Conv2d(in_channels = 3, out_channels = 3, kernel_size = 3, padding = 1),
			#nn.Conv2d(in_channels = 1, out_channels = 16, kernel_size = 3, padding = 1),
			nn.ReLU(),
			nn.BatchNorm2d(3),
			#nn.MaxPool2d(kernel_size=2, stride =2),

			#nn.MaxPool2d(kernel_size =2, stride = 2),
			#letting each image pass through the first 2 layers of the network without changing any dimensions

			nn.Conv2d(in_channels = 3, out_channels = 3, kernel_size = 3, padding = 1),
			nn.ReLU(),
			nn.BatchNorm2d(3),


			nn.Conv2d(in_channels = 3, out_channels = 16, kernel_size = 3, padding = 1),
			nn.LeakyReLU(),
			nn.AvgPool2d(kernel_size =2, stride = 2),
			nn.BatchNorm2d(16),

			nn.Conv2d(in_channels = 16, out_channels = 32, kernel_size = 3, padding = 1),
			nn.LeakyReLU(),
			nn.AvgPool2d(kernel_size =2, stride = 2),
			nn.BatchNorm2d(32),

			nn.Conv2d(in_channels = 32, out_channels = 64, kernel_size = 3, padding = 1),
			nn.ReLU(),
			nn.AvgPool2d(kernel_size =2, stride = 2),
			nn.BatchNorm2d(64),

			nn.Conv2d(in_channels = 64, out_channels = 128, kernel_size = 3, padding = 1),
			nn.ReLU(),
			nn.AvgPool2d(kernel_size =2, stride = 2),
			nn.BatchNorm2d(128),

			nn.Flatten(),

			#nn.Conv2d(in_channels = 32, out_channels = 64, kernel_size = 3, padding = 1),
			nn.Linear(128*2*2, 128),

			nn.ReLU(),
			#nn.Dropout(p=0.2),

			nn.Linear(128,2)
			)

	def forward(self, x):
		logits = self.stack(x)
		return logits

seek = Seek()
seek.load_state_dict(torch.load('steg_model.pth', weights_only = True))
seek.eval()

"""
def trainloop(original, loss_fn, optimizer, message, messagevec):
	stego_image1 = hide(original, message)
	loss =  10*loss_fn(stego_image1, original)
	decoded = urit(stego_image1)
	pred = seek(stego_image1)
	messagevec = messagevec.unsqueeze(0).float()
	loss2 = nn.BCEWithLogitsLoss()(decoded, messagevec)
	pred = seek(stego_image1)
	loss3 = nn.CrossEntropyLoss()(pred, torch.tensor([0]))
	loss = loss + loss2 + loss3
	optimizer.zero_grad()
	loss.backward()
	optimizer.step()
	return stego_image1, loss.item()
"""

def trainloop(original, loss_fn, optimizer, message, messagevec, epoch):
	stego_image1 = hide(original, message)
	
	loss1 = loss_fn(stego_image1, original)
	
	decoded = urit(stego_image1)
	messagevec_padded = messagevec.unsqueeze(0).float()
	loss2 = nn.BCEWithLogitsLoss()(decoded, messagevec_padded)
	
	pred = seek(stego_image1)
	loss3 = nn.CrossEntropyLoss()(pred, torch.tensor([1])) 
	
	if epoch < 1000:
		loss = loss2
	else:
		loss = (18.0 * loss1) + loss2 + (0.5 * loss3)
		
	optimizer.zero_grad()
	loss.backward()
	optimizer.step()
	return stego_image1, loss.item()

transform = transforms.ToTensor()

image = Image.open("07488.png").convert("RGB")
image = transform(image)
image = image.unsqueeze(0)
current = image
loss_fn1 = nn.MSELoss()
learning_rate = 1e-5
optimizer = torch.optim.AdamW(list(hide.parameters()) + list(urit.parameters()), lr = learning_rate)

"""
for i in range(5000):
	message = message_bank_strings[random.randint(0,99)]
	messagevec = [int(x) for x in message]
	messagevec = torch.tensor(messagevec)
	current, loss = trainloop(image, loss_fn1, optimizer, message, messagevec)
	if i %100 == 0:
		print("current loss:", loss)
"""

for i in range(10000):
	message = message_bank_strings[random.randint(0,99)]
	messagevec = [int(x) for x in message]
	messagevec = torch.tensor(messagevec)
	
	current, loss = trainloop(image, loss_fn1, optimizer, message, messagevec, epoch=i)
	
	if i % 100 == 0:
		print(f"current combined loss: {loss:.6f}")


save_image(current, "steg5.png")

with torch.no_grad():
	decoded2 = urit(current)
	print(decoded2)
	print(messagevec)
	messagevec = messagevec.unsqueeze(0).float()
	message_loss = nn.BCEWithLogitsLoss()(decoded2, messagevec)
	decoded_binary = (decoded2 > 0.0).int().squeeze(0)
	true_binary = messagevec.squeeze().int()
	correct_bits = (decoded_binary == true_binary).sum().item()
	print("message loss final: " + str(message_loss.item()))
	print(f"Extraction Accuracy: {correct_bits}/ 44 bits ({(correct_bits / 44) * 100:.1f}%)")
#low message_loss indicates that the message was accurately decoded.
#needed to put it here at the end so tht I could use a trained Urit to read the image. 


print("done!")

