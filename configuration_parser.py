import configparser
import os
import subprocess
import sys
from subprocess import Popen, PIPE

### Fetching and assigning the command line argument  ###
profileName = sys.argv[1]

### Exception Handling ###
try:
    print(subprocess.check_output(['./test.sh', 'test'], shell=True))
except Exception as e:
    print(e)

### Configuration parser ###
config = configparser.ConfigParser()
config.read("config.ini")
aws_access_key_id = config.get(profileName, "aws_access_key_id")
aws_secret_access_key = config.get(profileName, "aws_secret_access_key")
aws_session_token = config.get(profileName, "aws_session_token")
os.environ["AWS_ACCESS_KEY_ID"] = aws_access_key_id
os.environ["AWS_SECRET_ACCESS_KEY"] = aws_secret_access_key
os.environ["AWS_SESSION_TOKEN"] = aws_session_token
print(os.environ['AWS_ACCESS_KEY_ID'])
print(os.environ['AWS_SECRET_ACCESS_KEY'])
print(os.environ['AWS_SESSION_TOKEN'])
