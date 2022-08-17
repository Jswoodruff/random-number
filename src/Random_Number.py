import random
import pandas as pd
import numpy as np
import os 
from pathlib import Path
import warnings

warnings.filterwarnings("ignore")


filepath2 = os.path.join(Path(__file__).parents[1], 'data\SBI SMART Report MTD 7.22 to 8.13.22 Team (1).xlsx')
filepath1 = os.path.join(Path(__file__).parents[1], 'data\TechOps_Responses_20220816_071451.xlsx')

def run_app():

    # Import Raffle DF
    raffle = pd.read_excel(
       filepath1, 
        skiprows=2,
        header=0)
    # Select Columns / Remove noisy data
    raffle = raffle[['Tech ID', 'SMS tNPS']]
    # Import Master List
    master = pd.read_excel(
        filepath2,
        sheet_name=-1)
    # Select Columns / Remove noisy data
    master = master[["Tech ID", "Last Name, First Name", "Company"]]

    # Merge data sets
    d = raffle.merge(master, how="left", on="Tech ID")

    # Limit Scores to 9 and 10 only
    top_scores = d[d['SMS tNPS'] >= 9]

    # Format First name Last name instead of Last name First name
    top_scores['First Name'] = top_scores["Last Name, First Name"].str.split(
        ',', expand=True)[1]
    top_scores['Last Name'] = top_scores["Last Name, First Name"].str.split(
        ',', expand=True)[0]
    top_scores['Tech Name'] = top_scores['First Name'] + \
        ' ' + top_scores['Last Name']

    # Random dice roll count
    dice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    roll_count = np.random.choice(dice)

    # Randomize the DF
    for num in range(roll_count):
        top_scores = top_scores.sample(frac=1)

    # Print top 20 techs after randomization 
    
    my_string = f'This was randomized {roll_count} times! These are the winners of todays raffle.'
    winners = top_scores.sample(20)[['Tech ID', 'Tech Name', 'Company']]

    final = []

    for winner in winners.iterrows():
        final.append(str(winner[1]['Tech ID']) + ' - ' + winner[1]
            ['Tech Name'] + ' - ' + winner[1]['Company'])

    return my_string, final

if __name__ == '__main__':
    print(run_app())
