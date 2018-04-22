from tpot import TPOTClassifier
import constants as cn
import numpy as np
import DataManager as dm

tpot_config = {
		'sklearn.ensemble.RandomForestClassifier': {
			'n_estimators': [10, 20, 30, 40, 50, 100, 500, 1000],
			'criterion': ["gini", "entropy"],
			'max_depth': ["None", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
			'min_samples_split': [2, 3, 4, 5, 6, 7, 8, 9, 10],
			'min_samples_leaf': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
			'min_weight_fraction_leaf': [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
			'max_leaf_nodes': ["None", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
			'min_impurity_decrease': [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],			
			'class_weight': ["balanced", "balanced_subsample"]
		}
	}

"""	Find the best pipeline with TPOT and export the code """
def TPOT_Optimize(X_train, y_train, export):
	clf = TPOTClassifier(generations=3, verbosity=2, config_dict=tpot_config)
	clf.fit(X_train, y_train)
	
	if (export):
		clf.export(cn.TPOT_exported_file_name)


""" Start TPOT process """
def start_TPOT_optimizing(export, samples):
	X_train, y_train, _, _ = dm.train_test_set_generator(samples=samples)

	TPOT_Optimize(X_train, y_train, export)