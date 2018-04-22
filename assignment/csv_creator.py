import glob
import csv
import pandas as pd
import constants as cn

def csv_headers():
	with open(cn.whole_dataset_name, "wb") as csvfile:
		w = csv.writer(csvfile)
		w.writerow(["path", "alphabet", "character_number", "class_id"])
	
	with open(cn.train_dataset_name, "wb") as csvfile:
		w = csv.writer(csvfile)
		w.writerow(["path", "alphabet", "character_number", "class_id"])
	
	with open(cn.test_dataset_name, "wb") as csvfile:
		w = csv.writer(csvfile)
		w.writerow(["path", "alphabet", "character_number", "class_id"])

def csv_create(path, alphabet, character_number, class_id, flag):	
	if (flag == 0):
		with open(cn.whole_dataset_name, "a") as csvfile:
			w = csv.writer(csvfile)
			w.writerow([path, alphabet, character_number, class_id])
    
	elif (flag == 1):
		with open(cn.train_dataset_name, "a") as csvfile:
			w = csv.writer(csvfile)
			w.writerow([path, alphabet, character_number, class_id])
	
	elif (flag == 2):
		with open(cn.test_dataset_name, "a") as csvfile:
			w = csv.writer(csvfile)
			w.writerow([path, alphabet, character_number, class_id])

def path_parser(l1, l2, l3):
	class_id = 0
	path = l1[0]
	tree = path.split("/")
	char_temp = tree[-2]
	csv_create(path, tree[-3], tree[-2], 0, 0)

	#write whole dataset
	for i in range(1, len(l1)):
		path = l1[i]
		tree = path.split("/")
		if(tree[-2] != char_temp):
			class_id += 1
			char_temp = tree[-2]
		csv_create(path, tree[-3], tree[-2], class_id, 0)

	training_alphabets = cn.training_alphabets 
	test_alphabets = cn.test_alphabets
	training_samples = cn.training_samples
	test_samples = cn.test_samples

	train_alph_count = 0
	test_alph_count = 0
	char_count = 0
	train_alph_full = 0
	test_alph_full = 0
	char_full = 0
	general_count = 0

	#write training_set
	path = l2[0]
	tree = path.split("/")
	alph_temp = tree[-3]
	char_temp = tree[-2]
	class_id = 0
	csv_create(path, tree[-3], tree[-2], 0, 1)
	char_count += 1
	
	for i in range(1, len(l2)):
		path = l2[i]
		tree = path.split("/")
		alphabet = tree[-3]
		character_number = tree[-2]		
				
		if(train_alph_full == 0):
			if(alphabet != alph_temp):
				train_alph_count += 1
				alph_temp = alphabet
			if(train_alph_count >= training_alphabets):
				train_alph_full = 1								
				break			
			if(character_number != char_temp):
				class_id += 1
				csv_create(path, tree[-3], tree[-2], class_id, 1)				
				char_full = 0
				char_count = 1
				general_count += 1
				char_temp = character_number 
			else:
				if(char_full == 0):
					csv_create(path, tree[-3], tree[-2], class_id, 1)	
					general_count += 1				
					char_count += 1
				if(char_count >= training_samples):
					char_full = 1

	print("%d items in training_set" % general_count)

	#write test set
	path = l3[0]
	tree = path.split("/")
	alph_temp = tree[-3]
	char_temp = tree[-2]
	char_count = 0
	char_full = 0
	general_count = 0
	class_id += 1

	for i in range(0, len(l3)):
		path = l3[i]
		tree = path.split("/")
		alphabet = tree[-3]
		character_number = tree[-2]									
		
		if(test_alph_full == 0):
			if(alphabet != alph_temp):
				test_alph_count += 1
				alph_temp = alphabet
			if(test_alph_count >= test_alphabets):
				test_alph_full = 1				
				print("%d items in test_set" % general_count)							
				break

			if(character_number != char_temp):
				class_id += 1
				csv_create(path, tree[-3], tree[-2], class_id, 2)	
				general_count += 1			
				char_full = 0
				char_count = 1
				char_temp = character_number 
			else:
				if(char_full == 0):
					csv_create(path, tree[-3], tree[-2], class_id, 2)	
					general_count += 1				
					char_count += 1
				if(char_count >= test_samples):
					char_full = 1

def create_datasets():	
	l1 = glob.glob("Omniglot/*/*/*/*")
	l2 = glob.glob("Omniglot/images_background/*/*/*")
	l3 = glob.glob("Omniglot/images_evaluation/*/*/*")

	csv_headers()
	path_parser(l1, l2, l3)