from PIL import Image, ImageChops
import numpy as np
from skimage.filters.rank import enhance_contrast_percentile
from skimage.morphology import disk


"""	Load image as Image from "path" """
def load_image(path):
	 return Image.open(path)


"""	Get the object from the images and create a new image representing
	the differences between the two images overlapped """
def process_images(img1, img2):
	"""
	img1, img2:	input images in Image format

	return:		value representing how much the 2 images
				look similar
	"""

	#	get the size of original the image
	img_dim = img1.getbbox()

	#	invert the bit of the pixels
	img1_inv = ImageChops.invert(img1)
	img2_inv = ImageChops.invert(img2)

	#	get the object from the 2 images
	box1 = img1_inv.getbbox()
	box2 = img2_inv.getbbox()

	#	crop the object from the images
	img1_obj = img1_inv.crop(box1)
	img2_obj = img2_inv.crop(box2)

	#	resize the 2nd image according to the object of the 1st image
	img2_obj = img2_obj.resize((box1[2]-box1[0], box1[3]-box1[1]))

	#	enhance the simplicity of the objects (take an array and return an array)
	obj1_simple = enhance_contrast_percentile(np.array(img1_obj), disk(3), p0=.8, p1=.9)
	obj2_simple = enhance_contrast_percentile(np.array(img2_obj), disk(3), p0=.8, p1=.9)

	#	convert the objects from array to image
	img1_obj = Image.fromarray(obj1_simple)
	img2_obj = Image.fromarray(obj2_simple)

	#	invert the bit of the pixels of the 2nd image
	img2_obj = ImageChops.invert(img2_obj)

	#	generate a new image representing the one inside the other
	img_diff = ImageChops.invert(ImageChops.add_modulo(img1_obj, img2_obj))

	#	resize the new image into the old sizes	
	img_diff = img_diff.resize((img_dim[2]-img_dim[0], img_dim[3]-img_dim[1]))	

	return np.count_nonzero(np.array(img_diff))