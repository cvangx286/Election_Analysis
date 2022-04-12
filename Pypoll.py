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

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader= csv.reader(election_data)

   # Print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)
