import subprocess
import sqliite3
import time

REPO_PATH="git@github.com:markmcwiggins/testautomation"

def check_for_git_changes(repo_path):
    while True:
        try:
            # Get the hash of the latest commit
            latest_commit_hash = subprocess.check_output(["git", "log", "-1", "--format=%H"], cwd=repo_path, text=True).strip()

            # Check if the hash has changed since the last check
            if latest_commit_hash != check_for_git_changes.last_commit_hash:
                print("Change detected in the Git repository!")

                subprocess.run(["python", "test_program.py"], cwd=repo_path)

                # Update the last commit hash
                check_for_git_changes.last_commit_hash = latest_commit_hash
            else:
                print("No change detected.")

        except subprocess.CalledProcessError as e:
            print("Error:", e)

        time.sleep(10)  # Check every 10 seconds

if __name__ == "__main__":
    repository_path = "/path/to/your/git/repository"
    check_for_git_changes.last_commit_hash = ""  # Initialize last commit hash
    check_for_git_changes(repository_path)
