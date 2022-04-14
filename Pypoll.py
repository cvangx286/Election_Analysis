#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each canidate won
#4. the total number of votes each candidate won
#5. the winner of the election based on popular vote. 
# import datetime
# now = datetime.datetime.now()
# print("The time right now is ", now)
# Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'
# # Open the election results and read the file.
# with open(file_to_load) as election_data:

# # To do: perform analysis.

#     print(election_data)

#Import the csv and os modules.
# import csv
# import os

# #Add the filename variable that references the path to election_results.csv. (Assign a variable for the file to load and the path.)
# file_to_load = os.path.join("Resources", "election_results.csv")

# #Open the election_results.csv using the with statement as the filename object, election_data.

# with open(file_to_load) as election_data

# #Print the filename object.
#     print(election_data)

# import csv
# import os

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Use the open statement to open the file as a text file.
# outfile = open(file_to_save, "w")

# # Write some data to the file.
# outfile.write("Hello World")

# # Close the file
# outfile.close()

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis","election_analysis.txt")
# # print(file_to_save)

# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     # # Write some data to the file.
#     # txt_file.write("Arapahoe, ")
#     # txt_file.write("Denver, ")
#     # txt_file.write("Jefferson")
#     txt_file.write("Counties in the Election\n----------------------\n")
#     txt_file.write("Arapahoe\nDenver\nJefferson")

#3.4.4 module 3
    # Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes
candidate_options = []

# 1. Declare the empty dictionary.
candidate_votes = {}

# Declare a variable that holds an empty string value for the winning candidate.
winning_candidate = ""

# Declare a variable for the "winning count" equal to zero.
winning_count = 0 

# Declare a variable for the "winning_percentage" equal to zero.
winning_percentage = 0 

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader= csv.reader(election_data)

   # Print the header row.
    headers = next(file_reader)
        # print(headers)
  
    #Print each row in the CSV file.
    for row in file_reader:
       # print(row)

        total_votes = total_votes +1
    
     # Print the candidate name from each row
        candidate_name = row[2]

# If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

 # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

  # Add a vote to that candidate's count.
        candidate_votes[candidate_name] = candidate_votes[candidate_name]+ 1
        
    for candidate_name in candidate_votes:

                # 2. Retrieve vote count of a candidate.    
        votes = candidate_votes[candidate_name]

            # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

    # # 4. Print the candidate name and percentage of votes.
        # print(f"{candidate_name}: received {vote_percentage}% of the vote.")

#  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
                    # If true then set winning_count = votes and winning_percent =
                    # vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
                    # And, set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name

        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
      
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
print(winning_candidate_summary)

# Print the candidate vote dictionary.
# print(candidate_votes)

# print(candidate_options)


# print(total_votes)
