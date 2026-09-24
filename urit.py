import torch
from torch import nn
from torchvision import datasets
from torch.utils.data import DataLoader
from torchvision.transforms import v2


class decoder(nn.Module):
	def __init__(self):
		super().__init__()
		self.stack = nn.Sequential(

			nn.Conv2d(in_channels = 3, out_channels = 16, kernel_size = 3, padding = 1),
			nn.ReLU(),
			nn.MaxPool2d(kernel_size=2, stride =2),

			nn.Conv2d(in_channels = 16, out_channels = 32, kernel_size = 3, padding = 1),
			nn.ReLU(),
			nn.MaxPool2d(kernel_size =2, stride = 2),

			
			nn.Conv2d(in_channels = 32, out_channels = 64, kernel_size = 3, padding = 1),
			nn.ReLU(),
			nn.MaxPool2d(kernel_size =2, stride = 2),

			nn.Conv2d(in_channels = 64, out_channels = 128, kernel_size = 3, padding = 1),
			nn.ReLU(),
			nn.MaxPool2d(kernel_size =2, stride = 2),

			nn.Flatten(),

			nn.Linear(128*2*2, 128),
			nn.ReLU(),

			nn.Linear(128,44)	
			)

	def forward(self, x):
		logits = self.stack(x)
		return logits

urit = decoder()





