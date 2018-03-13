# Full Credit to https://github.com/carpedm20/DCGAN-tensorflow 
# I made a few modifications - mainly the center_crop function.

import matplotlib.pyplot as plt
import numpy as np
import scipy.misc


def imread(path, grayscale = False):
	if (grayscale):
		return scipy.misc.imread(path, flatten = True).astype(np.float)
	else:
		return scipy.misc.imread(path).astype(np.float)

def center_crop(x, resize_h=64, resize_w=64):
	h, w = x.shape[:2]

	if h > w:
		divisor = int((h - w) / 2)
		x = x[divisor:-divisor,:,:]
	elif w > h:
		divisor = int((w - h) / 2)
		x = x[:,divisor:-divisor,:]

	return scipy.misc.imresize(x, [resize_h, resize_w])

def get_image(image_path, resize_height=64, resize_width=64, crop=True, grayscale=False, normalize=True):
	
	image = imread(image_path, grayscale)
	
	return transform(image, resize_height, resize_width, crop, normalize=normalize)

def transform(image, resize_height=64, resize_width=64, crop=True, normalize=True):
	
	if crop:
		cropped_image = center_crop(image, resize_height, resize_width)
	else:
		cropped_image = scipy.misc.imresize(image, [resize_height, resize_width])

	if normalize:
		return np.array(cropped_image)/127.5 - 1.
	else:
		return np.array(cropped_image)