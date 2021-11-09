# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Import the datetime class from the dateline module
# import datetime as dt
# # Use the now() attribute on the datetime class to get the present time
# now = dt.datetime.now()
# print("The time right now is ", now)

# Assign a variable for the file to load and the path
# file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file
# with open(file_to_load) as election_data:

#     # To do: perform analysis
#     print(election_data)

# Import dependencies
import csv
import os


# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a file name variable to save the file
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Add total vote counter and set to 0
total_votes = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: read and analyze the data here
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    # Read the header row
    headers = next(file_reader)
    
    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
    
    # Print the total votes
    print(total_votes)




# Use the with statement to open the file as a text file
with open(file_to_save, "w") as txt_file:

    # Write some data to the file
    txt_file.write("Counties in the Election\n")
    txt_file.write('-'*25)
    txt_file.write("\nArapahoe\nDenver\nJefferson")