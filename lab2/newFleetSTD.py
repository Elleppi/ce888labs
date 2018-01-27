import matplotlib
matplotlib.use('Agg')

import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np

if __name__ == "__main__":
	df = pd.read_csv('./vehicles.csv')
	data = df["New Fleet"]

	print("Mean: %f")%(np.mean(data))
	print("Median: %f")%(np.median(data))
	print("Var: %f")%(np.var(data))
	print("std: %f")%(np.std(data))