import os
import sys
import requests
import json
from dotenv import load_dotenv

load_dotenv()

gitToken = os.getenv("GIT_TOKEN")
gitUsername = os.getenv("GIT_USERNAME")

if len(os.listdir('.')) == 0:
    if len(sys.argv) < 3:
        print("No arguments")
    else:
        boilerplate = sys.argv[1]
        projectName = sys.argv[2]
        private = sys.argv[3]

        command = {
            "name": projectName,
            "private": bool(private == "true"),
        }

        resp = requests.post(
            'https://api.github.com/user/repos', json=command, auth=(gitUsername, gitToken))

        y = json.loads(resp.text)

        print(resp.json()["clone_url"])

else:
    print("Directory is not empty")
