from PIL import Image
import numpy as np
import pandas as pd
from tpot import TPOTClassifier

def normalize_image(image):
    """
    Normalize image between 0 and 1.

    :param image: 1D list representing an image.
    :return: 1D list representing an image.
    """
    for i, pixel in enumerate(image):
        if pixel != 0:
            image[i] = 1
    return image

def load_image(path):
    """
    Load an image given a path.

    :param path: path to an image:
    :return: 1D list representing an image.
    """
    image = np.array(Image.open(path).getdata())
    return normalize_image(image)

df = pd.read_csv("omniglot_dataset.csv")
X = []
y = []

def image_comparison(img1, img2):
	X_list = []
	y_list = []

	X_list.append([load_image(df.iloc[img1]["path"]), load_image(df.iloc[img2]["path"])])
	
	if(df.iloc[img1]["char_id"] == df.iloc[img2]["char_id"]):
		y_list.append(1)
	else:
		y_list.append(0)

	return X_list, y_list

for i in range(0, 1000):
	img1 = np.random.choice(range(0, len(df)), replace=True)
	img2 = np.random.choice(range(0, len(df)), replace=True)

	X, Y = image_comparison(img1, img2)

my_tpot = TPOTClassifier(generations=3, verbosity=2, max_eval_time_mins=0.04, population_size=50)
my_tpot.fit(np.array(X), np.array(y))

#my_tpot.score(X_test, y_test)		