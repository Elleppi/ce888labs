import TPOT_Manager as tpot
import csv_creator
import RandomForest_manager as rfm
import ResultsManager as rm


"""	Main function """
def main():
	#csv_creator.create_datasets()
	#tpot.start_TPOT_optimizing(export=True, samples=50000)
	clf = rfm.run_RandomForest(samples=50000)
	rm.run_predictions(clf=clf, n_test=400, N=20)


if __name__ == "__main__":
    main()