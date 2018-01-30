import matplotlib
matplotlib.use('Agg')

import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np

if __name__ == "__main__":
	df = pd.read_csv('./vehicles.csv')
	df = df.dropna()

	sns_plot = sns.lmplot(df.columns[0], df.columns[1], data=df, fit_reg=False)

	sns_plot.axes[0,0].set_ylim(0,)
	sns_plot.axes[0,0].set_xlim(0,)

	sns_plot.savefig("vehicles.png",bbox_inches='tight')
	sns_plot.savefig("vehicles.pdf",bbox_inches='tight')

	currentFleet = df.values.T[0]
	newFleet = df.values.T[1]

	plt.clf()
	sns_plot2 = sns.distplot(currentFleet, bins=20, kde=False, rug=True).get_figure()

	axes = plt.gca()
	axes.set_xlabel('Day') 
	axes.set_ylabel('Current Fleet')

	sns_plot2.savefig("CurrentFleetHistogram.png",bbox_inches='tight')
	sns_plot2.savefig("CurrentFleetHistogram.pdf",bbox_inches='tight')

	plt.clf()
	sns_plot3 = sns.distplot(newFleet, bins=20, kde=False, rug=True).get_figure()

	axes = plt.gca()
	axes.set_xlabel('Day') 
	axes.set_ylabel('New Fleet')

	sns_plot3.savefig("NewFleetHistogram.png",bbox_inches='tight')
	sns_plot3.savefig("NewFleetHistogram.pdf",bbox_inches='tight')