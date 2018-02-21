import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np

#Two images are the same if:
#	they belong to the same alphabet
#	they are the same character
def image_comparison(img1, img2, l):
	if(l.get_value(img1, "alphabet") - l.get_value(img2, "alphabet") == 0):
		if(l.get_value(img1, "character_number") - l.get_value(img2, "character_number") == 0):
			return 1 #the two images are the same
	return 0 #the two images are differents

df = pd.read_csv("training_set.csv", delimiter = ";")
#df = df[:100] #keep only the top 100 values
df_copy = df.copy()

del df_copy["path"]
del df_copy["image_name"]

df_copy[["alphabet"]] = df_copy[["alphabet"]].apply(LabelEncoder().fit_transform)
df_copy[["character_number"]] = df_copy[["character_number"]].apply(LabelEncoder().fit_transform)

combinations_number = 50000
same_count = 0
different_count = 0

for i in range(0, combinations_number):
	img1 = np.random.choice(range(0, len(df)), replace=True)
	img2 = np.random.choice(range(0, len(df)), replace=True)

	if(image_comparison(img1, img2, df_copy) == 1):
		same_count += 1
	else:
		different_count += 1

	#print("[%s <-> %s] ---> %d" % (df.get_value(img1, "image_name"), df.get_value(img2, "image_name"), image_comparison(img1, img2, df_copy)))

print("sample number: %d" % combinations_number)
print("different images: %d" % different_count)
print("same images: %d" % same_count)