import argparse
import pandas as pd
from collections import Counter

# Dictionary to convert 3-letter abbreviations into team names
all_teams = {
    'ANA': 'Anaheim Angels',                    # Existed from 1997-2004, became the Los Angeles Angels
    'ARI': 'Arizona Diamondbacks',
    'ATL': 'Atlanta Braves',
    'BAL': 'Baltimore Orioles',
    'BOS': 'Boston Red Sox',
    'BRO': 'Brooklyn Dodgers',                  # Moved to Los Angeles
    'BSN': 'Boston Braves',                     # Moved to Milwaukee in 1953, then moved to Atlanta in 1965
    'CAL': 'California Angels',                 # Renamed several times; now Los Angeles Angels
    'CHA': 'Chicago White Sox',
    'CHN': 'Chicago Cubs',
    'CLE': 'Cleveland Guardians',               # Formerly Indians
    'CIN': 'Cincinnati Reds',
    'COL': 'Colorado Rockies',
    'DET': 'Detroit Tigers',
    'FLO': 'Florida Marlins',                   # Existed from 1993-2011, renamed Miami Marlins
    'HOU': 'Houston Astros',
    'KC1': 'Kansas City Athletics',             # Existed from 1955-1968, formerly in Philadelphia, then moved to Oakland
    'KCA': 'Kansas City Royals',
    'LAA': 'Los Angeles Angels',
    'LAN': 'Los Angeles Dodgers',
    'ML4': 'Milwaukee Brewers (AL)',            # Milwaukee Brewers in the American League from 1970-1998
    'MIL': 'Milwaukee Brewers (modern)',        # Milwaukee Brewers after they moved to the National League in 1998
    'ML1': 'Milwaukee Braves',                  # Moved from Boston in 1953, moved to Atlanta in 1965
    'MIN': 'Minnesota Twins',
    'MIA': 'Miami Marlins',
    'MON': 'Montreal Expos',                    # Moved to Washington Nationals
    'NYA': 'New York Yankees',
    'NYN': 'New York Mets',
    'NY1': 'New York Giants',                   # Moved to San Francisco in 1958
    'OAK': 'Oakland Athletics',
    'PHA': 'Philadelphia Athletics',            # Existed from 1901-1955, moved to Kansas City in 1955
    'PHI': 'Philadelphia Phillies',
    'PIT': 'Pittsburgh Pirates',
    'SDN': 'San Diego Padres',
    'SEA': 'Seattle Mariners',
    'SE1': 'Seattle Pilots',                    # Existed in 1969 only, moved to Milwaukee in 1970 to become the Brewers         
    'SFN': 'San Francisco Giants',
    'SLA': 'St. Louis Browns',                  # Moved to Baltimore in 1954, renamed the Orioles
    'SLN': 'St. Louis Cardinals',
    'TBA': 'Tampa Bay Rays',
    'TEX': 'Texas Rangers',
    'TOR': 'Toronto Blue Jays',
    'WS1': 'Washington Senators (1901–1960)',   # Moved to Minnesota in 1961, renamed the Twins
    'WS2': 'Washington Senators (1961–1971)',   # Moved to Texas in 1972, renamed the Rangers
    'WAS': 'Washington Nationals'             
}

# Code to parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-y", "--year", default=2015)
# Retrieving the year value from the argument list
year = vars(parser.parse_args())['year']
# Convert the year value from a 'str' to an 'int'
year = int(year)

# Present welcome and prompt to user
print(f"The team with the most players selected as all-stars in {year} is...")

# Load CSV file into pandas DataFrame
df_allstar = pd.read_csv("AllstarFull.csv")
all_teams_list = list(df_allstar['teamID'])

# Filter DataFrame by year input
df_filtered = df_allstar[df_allstar['yearID'] == year]

# Convert teamID column into list for processing
teamID_list = list(df_filtered['teamID'])
# Use Counter object to assemble dictionary with counts for each unique value in teamID_list
results = Counter(teamID_list)

# Checking if there is a tie between TWO teams with the highest number of all-stars
team_one, team_two = results.most_common(2)
# NOTE: results.most_common(2) returns two tuples of the teams with the highest number of all-stars

# Extract the number of players on the team(s) with the highest number of all-stars
num_all_stars = team_one[1]

# Print out list with conversion into team name(s)
if team_one[1] == team_two[1]:
    print(f"The {all_teams[team_one[0]]} and {all_teams[team_two[0]]} with {num_all_stars} MLB all-stars")    
else:
    print(f"The {all_teams[team_one[0]]} with {num_all_stars} MLB all-stars")
