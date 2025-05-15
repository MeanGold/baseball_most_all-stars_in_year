# baseball_most_all-stars_in_year
## About the repo

Using some data from the Baseball Databank dataset on Kaggle, I wrote a python script to find the team with the highest number of all-star selections in a given year between 1933-2015.

## Running the script
1. Download both the python script and the CSV file in the repo to your device, and save them to their own folder. 
2. Open a command prompt and navigate to the folder with the script and CSV file.<br/>

NOTE: You must run the script in the same directory as the CSV file otherwise you will get a file not found error when running the script

3. Run the script using the following code...
```
python most_all_stars_by_team_for_year.py -y {input_year}
```
OR
```
python most_all_stars_by_team_for_year.py --year {input_year}
```
NOTE: The code defaults the year to 2015 if no year is given or no argument is specified.


## Example output
Example output...<br/>
<img width="614" alt="image" src="https://github.com/user-attachments/assets/69cc2ad5-65fc-4395-93cc-8b8696be954d" />

I also added code to check if there are two teams that share the highest number of all-stars. Example from that output is below...<br/>
<img width="621" alt="image" src="https://github.com/user-attachments/assets/a9d38b73-0480-4f57-bf29-6c271953b4b3" />

## Dependencies
You will need to have **python** and **pandas** both installed on your machine.

NOTE: I fixed several mistakes in the original data file (AllstarFull.csv). There were a few typos in the teamID column that I had to manually fix in order to properly display the team names. For example, row 4680 was incorrectly labeled with a teamID of "ARL". After doing some research online, I found that this row corresponded to the Atlanta Braves all-star Jonny Venters in 2011, so instead the teamID should have been "ATL". I corrected this and a couple other errors that I found to help with outputting the name from my script. 
