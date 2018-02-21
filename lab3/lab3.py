import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import make_scorer
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score as acc

df = pd.read_csv("bank-additional-full.csv", delimiter=";")
df = df.dropna()

df_dummies = pd.get_dummies(df)


del df_dummies["duration"]
del df_dummies["y_no"]

plt.clf()
sns_plot = sns.distplot(df_dummies["y_yes"], bins = 20, kde=False, rug=False).get_figure()
sns_plot.savefig("y_yes_histogram.png",bbox_inches='tight')

all_columns = df_dummies.columns.tolist()
features = all_columns[:-1]
overcome = all_columns[-1]

X_df = df_dummies[features].copy()
y_df = df_dummies[overcome].copy()

X = X_df.values
y = y_df.values
clf = ExtraTreesClassifier(n_estimators = 100, max_depth = 4)

clf.fit(X, y)

scores = cross_val_score(clf, X, y, cv=10, scoring = make_scorer(acc))
print("ACC: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std()))

importances = clf.feature_importances_
std = np.std([tree.feature_importances_ for tree in clf.estimators_], axis=0)
indices = np.argsort(importances)[::-1]
print(indices)
print("Feature ranking:")

for f in range(X.shape[1]):
	print("%d. %s (%f)" % (f + 1, features[indices[f]], importances[indices[f]]))

fig = plt.figure()
plt.title("Feature importances")
plt.bar(range(X.shape[1]), importances[indices], color="r", yerr=std[indices], align="center")
plt.xticks(range(X.shape[1]), np.array(features)[indices])
plt.xlim([-1, X.shape[1]])
fig.set_size_inches(15, 8)
axes = plt.gca()
axes.set_ylim([0, None])

plt.savefig("importances.png", bbox_inches="tight")