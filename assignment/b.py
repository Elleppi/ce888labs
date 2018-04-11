import pandas as pd
from tpot import TPOTClassifier

df_train = pd.read_csv("training_set.csv")
df_test = pd.read_csv("test_set.csv")

outcome = ["char_id"]

y_train = df_train[outcome].copy()
y_test = df_test[outcome].copy()

del df_train["path"]
del df_train["image_name"]
del df_train["char_id"]

del df_test["path"]
del df_test["image_name"]
del df_test["char_id"]

dummies_train = pd.get_dummies(df_train, prefix = "", prefix_sep = "")
dummies_test = pd.get_dummies(df_test, prefix = "", prefix_sep = "")

dummies_train2, dummies_test2 = dummies_train.align(dummies_test, axis = 1, fill_value = 0)

X_train = dummies_train2.values
y_train = y_train.values

X_test = dummies_test2.values
y_test = y_test.values

my_tpot = TPOTClassifier(generations=3, verbosity=2, max_eval_time_mins=0.04, population_size=50)
my_tpot.fit(X_train, y_train)