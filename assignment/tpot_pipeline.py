import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# NOTE: Make sure that the class is labeled 'target' in the data file
tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
features = tpot_data.drop('target', axis=1).values
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'].values, random_state=42)

# Score on the training set was:0.8759
exported_pipeline = RandomForestClassifier(class_weight="balanced_subsample", criterion="entropy", max_depth=7, max_leaf_nodes=8, min_impurity_decrease=0.0, min_samples_leaf=8, min_samples_split=3, min_weight_fraction_leaf=0.0, n_estimators=500)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)
