
#converts the CIFAR-100 dataset into png images that can then be used in steganorgraphy

from pathlib import Path
import pickle
from PIL import Image

with open("cifar-100-python/train", "rb") as f:
    data = pickle.load(f, encoding="bytes")

images = data[b"data"]

output = Path("cifar100_png")
output.mkdir(exist_ok=True)

for i, img in enumerate(images):
    print("working")
    img = img.reshape(3, 32, 32).transpose(1, 2, 0)
    Image.fromarray(img).save(output / f"{i:05d}.png")

print("done!")