import configparser
import subprocess
from subprocess import Popen, PIPE
import os
### Receiving the header value
ProfileName = input("Enter the profile name ")
session = subprocess.Popen(['test.sh'], stdout=PIPE, stderr=PIPE)
stdout, stderr = session.communicate()
if stderr:
    raise Exception("Error "+str(stderr))
config = configparser.ConfigParser()
config.read("config.ini")
aws_access_key_id = config.get(ProfileName, "aws_access_key_id")
aws_secret_access_key = config.get(ProfileName, "aws_secret_access_key")
aws_session_token = config.get(ProfileName, "aws_session_token")
os.environ["AWS_ACCESS_KEY_ID"] = aws_access_key_id
os.environ["AWS_SECRET_ACCESS_KEY"] = aws_secret_access_key
os.environ["AWS_SESSION_TOKEN"] = aws_session_token
print(os.environ['AWS_ACCESS_KEY_ID'])
print(os.environ['AWS_SECRET_ACCESS_KEY'])
print(os.environ['AWS_SESSION_TOKEN'])
