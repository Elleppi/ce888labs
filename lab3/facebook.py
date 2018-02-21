import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import accuracy_score as acc
from sklearn.metrics import make_scorer
from sklearn.dummy import DummyRegressor
from sklearn.dummy import DummyClassifier
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("./dataset_Facebook.csv", delimiter = ";")

features = ["Category",
            "Page total likes",
            "Type",
            "Post Month",
            "Post Hour",
            "Post Weekday",
            "Paid"]

outcomes=  ["Lifetime Post Total Reach",
            "Lifetime Post Total Impressions",
            "Lifetime Engaged Users",
            "Lifetime Post Consumers",
            "Lifetime Post Consumptions",
            "Lifetime Post Impressions by people who have liked your Page",
            "Lifetime Post reach by people who like your Page",
            "Lifetime People who have liked your Page and engaged with your post",
            "comment",
            "like",
            "share",
            "Total Interactions"]

df[["Type"]] = df[["Type"]].apply(LabelEncoder().fit_transform)
df = df.dropna()

outcomes_of_interest = ["Lifetime Post Consumers", "like"]

X_df = df[features].copy()
y_df = df[outcomes_of_interest].copy()

cat_features = ["Category",
            "Type",

            "Paid"]


X_df = pd.get_dummies(X_df, columns = cat_features)

print X_df.head()[["Category_1", "Category_2","Category_3"]].to_latex()

X = X_df.values
y = y_df.values.T[0]

y = (y-y.min())/(y.max() - y.min())