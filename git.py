import os
import random
import subprocess
from datetime import datetime, timedelta

# Define the range for random days in the past year
days_in_past = 365  # Change this to how far back you want to go
number_of_commits = 50  # Change this to the number of random commits you want

# Create a new file or modify an existing one
filename = "random_commit.txt"
with open(filename, "a") as file:
    file.write("This is a random commit\n")

# Loop to make commits on random days in the past
for _ in range(number_of_commits):
    random_days_ago = random.randint(1, days_in_past)
    commit_date = datetime.now() - timedelta(days=random_days_ago)
    commit_date_str = commit_date.strftime('%Y-%m-%dT%H:%M:%S')

    # Set the date for the commit
    os.environ['GIT_COMMITTER_DATE'] = commit_date_str
    os.environ['GIT_AUTHOR_DATE'] = commit_date_str

    # Add, commit, and push the changes
    subprocess.run(["git", "add", filename])
    subprocess.run(["git", "commit", "-m", f"Commit on {commit_date_str}"])
    subprocess.run(["git", "push"])

print("Done! Your GitHub graph should now have more green squares.")
