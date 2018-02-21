import glob
import csv
import pandas as pd

def csv_headers():
	with open("omniglot_dataset.csv", "wb") as csvfile:
		w = csv.writer(csvfile, delimiter = ";")
		w.writerow(["path", "alphabet", "character_number", "image_name"])
	with open("training_set.csv", "wb") as csvfile:
		w = csv.writer(csvfile, delimiter = ";")
		w.writerow(["path", "alphabet", "character_number", "image_name"])
	with open("test_set.csv", "wb") as csvfile:
		w = csv.writer(csvfile, delimiter = ";")
		w.writerow(["path", "alphabet", "character_number", "image_name"])
	with open("validation_set.csv", "wb") as csvfile:
		w = csv.writer(csvfile, delimiter = ";")
		w.writerow(["path", "alphabet", "character_number", "image_name"])

def csv_create(path, alphabet, character_number, image_name, flag):	
	if (flag == 0):
		with open("omniglot_dataset.csv", "a") as csvfile:
			w = csv.writer(csvfile, delimiter = ";")
			w.writerow([path, alphabet, character_number, image_name])

	elif (flag == 1):
		with open("training_set.csv", "a") as csvfile:
			w = csv.writer(csvfile, delimiter = ";")
			w.writerow([path, alphabet, character_number, image_name])
	elif (flag == 2):
		with open("test_set.csv", "a") as csvfile:
			w = csv.writer(csvfile, delimiter = ";")
			w.writerow([path, alphabet, character_number, image_name])
	else:
		with open("validation_set.csv", "a") as csvfile:
			w = csv.writer(csvfile, delimiter = ";")
			w.writerow([path, alphabet, character_number, image_name])

def path_parser(l1, l2, l3):		
	#write whole dataset
	for i in range(0, len(l1)):
		path = l1[i]
		tree = path.split("/")
		csv_create(path, tree[-3], tree[-2], tree[-1], 0)


	training_alphabets = 30 #out of 50
	test_valid_alphabets = 10 #out of 50
	training_samples = 12 #out of 20
	test_valid_samples = 4 #out of 20
	train_alph_count = 0
	test_alph_count = 0
	valid_alph_count = 0
	char_count = 0
	train_alph_full = 0
	test_alph_full = 0
	valid_alph_full = 0
	char_full = 0
	general_count = 0

	#write training_set
	path = l2[0]
	tree = path.split("/")
	alph_temp = tree[-3]
	char_temp = tree[-2]
	
	for i in range(0, len(l2)):
		path = l2[i]
		tree = path.split("/")
		alphabet = tree[-3]
		character_number = tree[-2]
		image_name = tree[-1]
				
		if(train_alph_full == 0):
			if(alphabet != alph_temp):
				train_alph_count += 1
				alph_temp = alphabet
			if(train_alph_count >= training_alphabets):
				train_alph_full = 1		
				general_count += 1		
				break			
			if(character_number != char_temp):
				csv_create(path, tree[-3], tree[-2], tree[-1], 1)				
				char_full = 0
				char_count = 1
				general_count += 1
				char_temp = character_number 
			else:
				if(char_full == 0):
					csv_create(path, tree[-3], tree[-2], tree[-1], 1)	
					general_count += 1				
					char_count += 1
				if(char_count >= training_samples):
					char_full = 1

	print("%d items in training_set" % general_count)

	#write test set and validation set
	path = l3[0]
	tree = path.split("/")
	alph_temp = tree[-3]
	char_temp = tree[-2]
	char_count = 0
	char_full = 0
	general_count = 0

	for i in range(0, len(l3)):
		path = l3[i]
		tree = path.split("/")
		alphabet = tree[-3]
		character_number = tree[-2]
		image_name = tree[-1]						
		
		if(test_alph_full == 0):
			if(alphabet != alph_temp):
				test_alph_count += 1
				alph_temp = alphabet
			if(test_alph_count >= test_valid_alphabets):
				test_alph_full = 1
				char_count = 1
				char_full = 0
				char_temp = character_number
				csv_create(path, tree[-3], tree[-2], tree[-1], 3)
				general_count += 1
				print("%d items in test_set" % general_count)
				general_count = 1				
				continue

			if(character_number != char_temp):
				csv_create(path, tree[-3], tree[-2], tree[-1], 2)	
				general_count += 1			
				char_full = 0
				char_count = 1
				char_temp = character_number 
			else:
				if(char_full == 0):
					csv_create(path, tree[-3], tree[-2], tree[-1], 2)	
					general_count += 1				
					char_count += 1
				if(char_count >= test_valid_samples):
					char_full = 1
		elif(valid_alph_full == 0):
			if(alphabet != alph_temp):
				valid_alph_count += 1
				alph_temp = alphabet
			if(valid_alph_count >= test_valid_alphabets):
				valid_alph_full = 1		
				general_count += 1				
				break

			if(character_number != char_temp):
				csv_create(path, tree[-3], tree[-2], tree[-1], 3)	
				general_count += 1			
				char_full = 0
				char_count = 1
				char_temp = character_number 
			else:
				if(char_full == 0):
					csv_create(path, tree[-3], tree[-2], tree[-1], 3)		
					general_count += 1			
					char_count += 1
				if(char_count >= test_valid_samples):
					char_full = 1

	print("%d items in validation_set" % general_count)		

l1 = glob.glob("Omniglot/*/*/*/*")
l2 = glob.glob("Omniglot/images_background/*/*/*")
l3 = glob.glob("Omniglot/images_evaluation/*/*/*")
print("%d items in total" % len(l1)+1)

csv_headers()
path_parser(l1, l2, l3)