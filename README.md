# baseball_most_all-stars_in_year

Using some data from the Baseball Databank dataset on Kaggle, I wrote a python script to find the team with the highest number of all-star selections in a given year between 1933-2015.

NOTE: I fixed several mistakes in the original data file (AllstarFull.csv). There were a few typos in the teamID column that I had to manually fix in order to properly display the team names. For example, row 4680 was incorrectly labeled with a teamID of "ARL". After doing some research online, I found that this row corresponded to the Atlanta Braves all-star Jonny Venters in 2011, so instead the teamID should have been "ATL". I corrected this and a couple other errors that I found to help with outputting the name from my script. 
