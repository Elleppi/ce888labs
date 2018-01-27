import matplotlib
matplotlib.use('Agg')

import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np

if __name__ == "__main__":
	df = pd.read_csv('./vehicles.csv')
	
	sns_plot = sns.lmplot(df.columns[0], df.columns[1], data=df, fit_reg=False)

	sns_plot.axes[0,0].set_ylim(0,)
	sns_plot.axes[0,0].set_xlim(0,)

	sns_plot.savefig("VehiclesScaterplot.png",bbox_inches='tight')
	sns_plot.savefig("VehiclesScaterplot.pdf",bbox_inches='tight')

	data = df.values.T[0]

	print("Mean: %f")%(np.mean(data))
	print("Median: %f")%(np.median(data))
	print("Var: %f")%(np.var(data))
	print("std: %f")%(np.std(data))

	plt.clf()
	sns_plot2 = sns.distplot(data, bins=20, kde=False, rug=True).get_figure()

	axes = plt.gca()
	axes.set_xlabel('Current Fleet') 
	axes.set_ylabel('New Fleet')

	sns_plot2.savefig("VehiclesHistogram.png",bbox_inches='tight')
	sns_plot2.savefig("VehiclesHistogram.pdf",bbox_inches='tight')