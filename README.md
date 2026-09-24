This steganography project looks at building a generative adversarial network (GAN) to create steg images that are increasingly
difficult to detect, with inspiration drawn from the HiDDeN steg framework and SRNet architecture. 

There are 3 neural networks involved:
Hide embeds the 44-bit messages into the image.
Seek tries to determine whether the image is a steg image. 
Urit then tries to decode the message that Hide has embedded.

Lots of different least significant bit steganography techniques were used, including lsb matching, texture adaptive lsb, 
random lsb and random multi-bit lsb.

In order to train Seek, datasets were generated using the CIFAR-100 dataset. Pride and Prejudice was used to generate random
strings of 0s and 1s whilst making the datasets.

The lsb techniques mentioned above were used to embed 44-bit long messages inside images from the dataset, and Seek was randomly 
given either a steg or a original image to classify. A pre-trained Seek was then put into the neural network framework. Seek's 
training data and test data accuracy matched each other closely throughout, suggesting that Seek wasn't just memorising the dataset. 
Accuracy achieved on the test dataset was around 97.5%.

Urit trained at the same time as Hide, but losses from Hide and Seek weren't added until Urit had tried to decode 1000 messages.
This meant message extraction accuracy improved from around 50% to around 90%, measured by counting how many of the 44 
message bits were accurately recovered. To prevent Urit from memorising the message to decode, Hide randomly chose a message to
embed from a list of 100 possible messages. 

Hide's own loss measured the difference between the original image and the generated image, which forced Hide to embed messages in
a way that preserved the original image. 

Some example images that Hide generated are included in the generatedimages folder - stegs 1 to 5 are the result of 500, 1000, 2000,
5000 and 10,000 iterations respectively. 
