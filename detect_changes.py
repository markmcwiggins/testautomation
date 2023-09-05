#!/usr/bin/env python3

import subprocess
import time
import sqlite3

#REPO_PATH="git@github.com:markmcwiggins/testautomation"
REPO_PATH="."
con = sqlite3.connect('tutorial.db')
def check_for_git_changes(repo_path):
    while True:
        try:
            # Get the hash of the latest commit
            proc = subprocess.run(["./gitlog.sh"], text=True, capture_output=True)
            commitlines = proc.stdout.split('\n')
            print(commitlines)
            print(commitlines[0].strip().split())
            (fromstr, hash,weekday,  mo,  day, thyme, year) = commitlines[0].strip().split()
            (fromstr, firstname, lastname, email) = commitlines[1].strip().split()
            commitdate = commitlines[2].strip()
            subject = commitlines[3]. strip()
            print(email, commitdate, subject, hash)
            # Check if the hash has changed since the last check
            if hash != check_for_git_changes.last_commit_hash:
                print("Change detected in the Git repository!")

                subprocess.run(["python", "test_program.py"], cwd=repo_path)

                # Update the last commit hash
                check_for_git_changes.last_commit_hash = hash
            else:
                print("No change detected.")

        except subprocess.CalledProcessError as e:
            print("Error:", e)

        time.sleep(10)  # Check every 10 seconds

if __name__ == "__main__":
    repository_path = REPO_PATH
    check_for_git_changes.last_commit_hash = ""  # Initialize last commit hash
    check_for_git_changes(repository_path)
