## Analyzing Colorado voting data with Python
Analysis of 2018 U.S. House of Representatives election results for Colorado's District 1 to determine the winner

### Overview of Election audit
The project was completed in VS Code using Python to analyze a CSV file that contained a tally with the votes' ID numers, the county name and the candidate's name. The goal was to determine the total number of votes cast, create a complete list of the candidates who received votes, the percentage and total number of votes each candidate won, and establish the winner of the election based on popular vote.

### Resources
- Data source: election_results.csv
- Software: Python 3.8.8, Visual Studio Code 1.60.0

### **Findings**

The analysis of the election showed there were:
- 369,711 total votes cast
- The three counties in the precinct are:
    - Denver
    - Jefferson
    - Arapahoe
- The share of total votes by county were:
    - Denver: 306,055 votes, equal to 82.8% of the total votes
    - Jefferson: 38,855 votes, equal to 10.5% of the total votes
    - Arapahoe: 24,801 votes, equal to 6.7% of the total votes
- Voters from Denver represented by far the largest number of votes
- The candidates were:
    - Diana DeGette (DEM)
    - Charles Casper Stockham (REP)
    - Raymon Anthony Doane (LIB)
- The candidate results were:
    - Diana DeGette: 272,892 votes, equal to 73.8% of the total votes
    - Charles Casper Stockham: 85,213 votes, equal to 23% of the total votes
    - Raymon Anthony Doane: 11,606 votes, equal to 3.1% of the total votes
- The winner of the election was Diana DeGette with nearly three quarters of the votes

<img src ="https://user-images.githubusercontent.com/90064437/140976301-b8f90f4c-e75b-47a5-939e-d95266f444ba.png" width="400" height="">



### Election Audit Summary

The script developed for this analysis can easily be adapted for use for other election results. It can be used for larger elections that include a broader pool of candidates and a larger number of counties, as the script's `for` loop simply runs through the CSV file and finds any new variable thanks to the `.append()` function, then adds it to the total count via `+=1`.

Election results would need to be provided in a CSV file, but their format does not need to comply with that of the current CSV file, i.e. the voter ID, county and candidate columns do not need to be in the same order. The script can easily be changed to link up with different CSV files. The only thing that would need to be changed is the row count number currently listed as `candidate_name = row[2]`  and  `county_name = row[1]`  in the script.

Depending on how and where the CSV file is saved, the path to the file and the file name would need to be changed in the `os.path.join()` command to correspond with the right file path.

Depending on which election this file should be used for, the names of variables and the text output language can be adapted. For example, if this script is to be used for a municipal election, the variables could be changed for easier reading comprehension - but don't have to be! - to list the `winning_municipality` instead of the `winning_county`. The text in the text output file would need to be adapted accordingly to reflect the type of election.
