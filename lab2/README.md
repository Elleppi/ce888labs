# Lab2

## Scaterplot

I created a new python file named "vehicles.py" in which I: 
* Upload the data from the related csv file;
* Drop the NaN items from the imported file;
* Generate a common plot named "vehicles.png" ![scaterplot](./vehicles.png?raw=true) where you can see how the fleets are distributed
* Generate an histogram named "CurrentFleetHistogram.png" ![histogram](./CurrentFleetHistogram.png?raw=true) , by taking the first column of the data imported, where are displayed the occurrences for each current fleet day by day;
* Generate an histogram named "NewFleetHistogram.png" ![histogram](./NewFleetHistogram.png?raw=true), by taking the second column of the data imported, where are displayed the occurrences for each new fleet day by day.

## Standard Deviation

I created 2 files named "newFleetSTD.py" and "currentFleetSTD.py" where similarly for each one:
* Upload the csv file in a df variable;
* Drop the empty values;
* (newFleetSTD.py) Load in a variable all the values from the column named "new Fleet" and print Mean, Median, Variance and Standard Deviation for that values;
* (currentFleetSTD.py) Do the same for the column named "Current Fleet";

## Bootstrap

There are 2 files named "CurrentFleet_boot.py" and "NewFleet_boot.py" where similarly:
* Upload the data from the csv file and drop the empty elements;
* (CurrentFleet_boot.py) Load in a variable only the values included into the first column;
* (newFleetSTD.py) do the same by loading only the values included into the second column;
* Figure out the mean, lower bound and upper bound by applying the bootstrap function implemented equally in both of the file;
* Plot the result in file called "CurrentFleet_bootstrap.png" ![scaterplot](./CurrentFleet_bootstrap.png?raw=true) and "NewFleet_bootstrap.png" ![scaterplot](./NewFleet_bootstrap.png?raw=true)