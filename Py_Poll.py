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

# Add variable for candidates to collect names
candidate_options = []

# Add a dictionary to link votes to candidates
candidate_votes = {}

# Add winning candidate and winning account tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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

        # Print the candidate name from each row
        candidate_name = row[2]

        # Check if candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            # Begin tracking that candidates vote count
            candidate_votes[candidate_name] = 0
            # Increase increment count
        candidate_votes[candidate_name] += 1
    
    #Determine percentage of votes for each candidate by looping through the counts
    # Iterate through the candidate list
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # Calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # to do: print out each candidate's name, vote count, and percent of votes
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        #determine winning vote count and candidate
        # Determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true set winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        # print candidate name and percentage of votes
        # print(f"{candidate_name} has received {vote_percentage:.1f}% of the votes.")
    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------\n")
    print(winning_candidate_summary)
    
    # Print the result
    # print(total_votes)
    # print(candidate_votes)




# Use the with statement to open the file as a text file
with open(file_to_save, "w") as txt_file:

    # Write some data to the file
    txt_file.write("Counties in the Election\n")
    txt_file.write('-'*25)
    txt_file.write("\nArapahoe\nDenver\nJefferson")