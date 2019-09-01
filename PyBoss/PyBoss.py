#dependencies

import csv
import datetime

#file to load 
file_to_load = "Resources/employee_data.csv"
file_to_output = "Analysis/employee_data_reformatted.csv"

#dictionary of states with abbreviations
us_state_abbreviation = {
      "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}


#placeholders for re-formatted
emp_ids = []
emp_first_names = []
emp_last_names = []
emp_dobs = []
emp_ssns = []
emp_states = []


#read the csv and convert it into a list
with open(file_to_load) as employee_data:
   reader = csv.DictReader(employee_data)

   #loop through each row
   for row in reader:

     #store it into a list 
     emp_ids = emp_ids + [row["Emp ID"]]

     #spilt name store it in var
     split_name = row["Name"].split(" ")

     #save first and last name in separate list
     emp_first_names = emp_first_names + [split_name[0]]
     emp_last_names = emp_last_names + [split_name[1]]

     #reformate DOB
     reformatted_dob = datetime.datetime.strptime(row["DOB"], "%Y-%m-%d")
     reformatted_dob = reformatted_dob.strftime("%m%d%y")

     #store it into a list
     emp_dobs = emp_dobs + [reformatted_dob]

     #reformat SSN
     split_ssn = list(row["SSN"])
     split_ssn[0:3] = ("*", "*", "*")
     split_ssn[4:6] = ("*", "*")
     joined_ssn = "".join(split_ssn)

     #store into list
     emp_ssns = emp_ssns + [joined_ssn]

     #use dic to find replacement for state
     state_abbreviation = us_state_abbreviation[row["State"]]

     #store abbre into list
     emp_states = emp_states + [state_abbreviation]

#zip all new lists 
empbd = zip(emp_ids,emp_first_names,emp_last_names,emp_dobs,emp_ssns,emp_states)

#write election data to csv
with open(file_to_output, "w", newline="") as datafile:
  writer = csv.writer(datafile)
  writer.writerow(["Emp ID", "First Name", "Last Name", "DOB","SSN", "State"])
  writer.writerows(empbd)

  






