#import CSV file 


import csv

#files to load and output

file_to_load = "Resoures/election_data.csv"
file_to_output = "Analysis/election_analysis.txt"

#variables need to use to analyze the votes

total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0 

#read the csv file
with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)


#create a loop 
    for row in reader:

        print(",", end="")

        total_votes = total_votes + 1
        candidate_name = row["Candidate"]

        if candidate_name not in candidate_options:
           candidate_options.append(candidate_name)
           candidate_votes[candidate_name] = 0

        
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

        #print result to txt

    with open (file_to_output, "w") as txt_file:

        #print the final vote count to txt
        election_results = (
            f"\n\nElection Result\n"
            f"--------------------------\n"
            f"Total Votes: {total_votes}\n"
            f"--------------------------\n")
        print(election_results,end="")

        #save final vote to txt
        txt_file.write(election_results)

        #result of winners by looping through the counts
        for candidate in candidate_votes:

            #calculate vote count and percentage
            votes = candidate_votes.get(candidate)
            vote_percentage = float(votes) / float(total_votes)* 100

            #calculate winning vote 
            if (votes > winning_count):
                winning_count = votes
                winning_candidate = candidate

            #print individual voter count
            voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
            print(voter_output,end="")

            #save voter count to txt
            txt_file.write(voter_output)
        
        #print the winning candidate
        winning_candidate_summary =(
            f"---------------------------\n"
            f"Winner : {winning_candidate}\n"
            f"----------------------------\n")
        print(winning_candidate_summary)

        #save the winning candidate name to txt
        txt_file.write(winning_candidate_summary)





