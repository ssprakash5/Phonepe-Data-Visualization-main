import subprocess

# Define the URL of the GitHub repository
repo_url = 'https://github.com/phonepe/pulse.git'

# Define the local directory where you want to clone the repository
local_dir = "D:/phonepe data"

# Run the Git clone command
try:
    subprocess.run(['git', 'clone', repo_url, local_dir], check=True)
    print("Repository cloned successfully.")
except subprocess.CalledProcessError:
    print("Error cloning repository.")
