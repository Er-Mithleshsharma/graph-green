import os
import random
import subprocess
from datetime import datetime, timedelta

# Define the range for random days in the past year
days_in_past = 365  # Change this to how far back you want to go
number_of_commits = 50  # Change this to the number of random commits you want

# Create a file to track commits
filename = "random_commit.txt"

for i in range(number_of_commits):
    # Make a change to the file
    with open(filename, "a") as file:
        file.write(f"Commit number {i + 1}\n")

    # Choose a random date within the past year
    random_days_ago = random.randint(1, days_in_past)
    commit_date = datetime.now() - timedelta(days=random_days_ago)
    commit_date_str = commit_date.strftime('%Y-%m-%dT%H:%M:%S')

    # Set the date for the commit
    os.environ['GIT_COMMITTER_DATE'] = commit_date_str
    os.environ['GIT_AUTHOR_DATE'] = commit_date_str

    # Add, commit, and push the changes
    subprocess.run(["git", "add", filename])
    subprocess.run(["git", "commit", "-m", f"Commit on {commit_date_str}"])

# Push all the commits at once
subprocess.run(["git", "push", "origin", "main"])

print("Done! Your GitHub graph should now have more green squares.")
