import glob
import csv
import pandas as pd

#def csv_headers():
	#with open("omniglot_dataset.csv", "wb") as csvfile:
		#w = csv.writer(csvfile)
		#w.writerow(["path", "alphabet", "character_number", "image_name", "char_id"])
#
#def csv_create(path, alphabet, character_number, image_name, char_id):	
#	
	#with open("omniglot_dataset.csv", "a") as csvfile:
		#w = csv.writer(csvfile)
		#w.writerow([path, alphabet, character_number, image_name, char_id])
#
#def path_parser(l1):
	#char_id = 0
	#path = l1[0]
	#tree = path.split("/")
	#char_temp = tree[-2]
	#csv_create(path, tree[-3], tree[-2], tree[-1], 0, 0)
#
	##write whole dataset
	#for i in range(1, len(l1)):
		#path = l1[i]
		#tree = path.split("/")
		#if(tree[-2] != char_temp):
			#char_id += 1
			#char_temp = tree[-2]
		#csv_create(path, tree[-3], tree[-2], tree[-1], char_id, 0)		
#
#l1 = glob.glob("Omniglot/*/*/*/*")
##print("%d items in total" % len(l1)+1)
#
#csv_headers()
#path_parser(l1)
import pandas as pd
df = pd.read_csv("omniglot_dataset.csv")

def create_df(train_sample):
	df_train = pd.DataFrame()
	df_test = pd.DataFrame()

	for i in range (0, len(df), 20):
		df_train = df_train.append(df[i:(i+train_sample)])
		df_test = df_test.append(df[(i+train_sample):(i+20)])

	return df_train, df_test

df_train, df_test = create_df(15)

df_train.to_csv("training_set1.csv")
df_test.to_csv("test_set1.csv")