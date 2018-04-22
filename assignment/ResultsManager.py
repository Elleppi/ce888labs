import pandas as pd
import constants as cn
import DataManager as dm


""" return dataframe """
def load_dataframe(path):
	return pd.read_csv(path)


""" run n_test predictions for N_way One Shot Learning """
def run_predictions(clf, n_test, N):
	"""
	clf:		classifier learned
	n_test:		number of test to perform
	N:			N-1 different classes, only one example
	"""

	df = load_dataframe(cn.whole_dataset_name)

	right_counter = 0	

	for i in range(0, n_test):
		feature_list, target_list = dm.N_way_one_shot_learning(N, df, cn.general_samples)
		dm.shuffle_lists(feature_list, target_list)
		
		predictions = clf.predict(feature_list)
		
		for j in range(0, N):			
			if(predictions[j] == target_list[j]):
				right_counter += 1

	print("%d%% of correct answers" % ((100*right_counter)/(N*n_test)))