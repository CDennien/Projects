"""
A file directory setup program, designed to make starting a new university semester easy.
Created by Callum Dennien.
"""

import os

# Welcome User
print("Welcome To My University File Directory Creator.")
print("--- Created by Callum Dennien. \n")


# Gather Base Student Information
file_directory_path = input("Designated Directory Path (e.g. /Users/InsertName/OneDrive): ")
student_year = input("Year of Study (e.g. 1): ")
student_study_period = int(input("Current Study Period (e.g. 1): "))
student_subject_count = int(input("Number of Subjects Undergoing (e.g. 1): "))

# Expand Upon Student Information
subject_codes = []

for subject in range(student_subject_count):
    new_subject = input("Subject Code #" + str(subject + 1) + ": ")
    subject_codes.append(new_subject)

# Change Directory to Chosen Path
os.chdir(file_directory_path)

# Check if Year Directory Exists
is_dir = os.path.isdir(student_year)
if not is_dir:
    os.makedirs("Year {:02d}".format(int(student_year)))

# Change Directory to Year Path
os.chdir(os.path.join(file_directory_path, "Year {:02d}".format(int(student_year))))

# Check if Study Period Directory Exists
file_directory_name = "Study Period {:02d}".format(student_study_period)
is_dir = os.path.isdir(file_directory_name)
if not is_dir:
    os.makedirs(file_directory_name)

# Change Directory to Study Period Path
os.chdir(os.path.join(file_directory_path, "Year {:02d}".format(int(student_year)), file_directory_name))

# Create Weekly Folders
for subject in subject_codes:
    os.makedirs(os.path.join(os.getcwd(), subject))

    os.makedirs(os.path.join(os.getcwd(), subject, "Textbook"))

    for week in range (1, 14):
        os.makedirs(os.path.join(os.getcwd(), subject, "Week{:02d}".format(week)))
