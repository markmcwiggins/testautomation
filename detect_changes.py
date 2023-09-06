#!/usr/bin/env python3

import subprocess
import time
import sqlite3
import re

#REPO_PATH="git@github.com:markmcwiggins/testautomation"
REPO_PATH="."
con = sqlite3.connect('users.db')
cur = con.cursor()
def get_slack(email, hash):
    email2 = re.sub(r'<','', email)
    email3 = re.sub(r'>','',email2)
    
    params = (email3,)
    res = cur.execute("select slackid, hash from  email2slack where email = ?", params)
    fields = res.fetchone()
    print(fields)
    return fields
    
def check_for_git_changes(repo_path):
    while True:
        try:
            # Get the hash of the latest commit
            proc = subprocess.run(["./gitlog.sh"], text=True, capture_output=True)
            commitlines = proc.stdout.split('\n')
            (fromstr, hash,weekday,  mo,  day, thyme, year) = commitlines[0].strip().split()
            (fromstr, firstname, lastname, email) = commitlines[1].strip().split()
            commitdate = commitlines[2].strip()
            subject = commitlines[3]. strip()

            (slack_id, hash) = get_slack(email, hash)
            # Check if the hash has changed since the last check
            if hash != check_for_git_changes.last_commit_hash:
                print("Change detected in the Git repository!")

                result = subprocess.run(["python", "test_program.py"], cwd=repo_path)
                if result.returncode != 0:
                    print("running the slackbot")
                    subprocess.run(["python", "slackbot.py", email, hash])

                # Update the last commit hash
                check_for_git_changes.last_commit_hash = hash
                # grab the slack ID
                
            else:
                print("No change detected.")

        except subprocess.CalledProcessError as e:
            print("Error:", e)

        time.sleep(10)  # Check every 10 seconds

if __name__ == "__main__":
    repository_path = REPO_PATH
    check_for_git_changes.last_commit_hash = ""  # Initialize last commit hash
    check_for_git_changes(repository_path)
