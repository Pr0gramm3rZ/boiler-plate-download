import os
import sys
import requests
import json
from dotenv import load_dotenv

load_dotenv()

gitToken = os.getenv("GIT_TOKEN")
gitUsername = os.getenv("GIT_USERNAME")


def getBoiler(i):
    switcher = {
        'react-native': 'react-redux-bolier-plate'
    }
    return switcher.get(i, "No boiler plate")


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

        boilerName = getBoiler(boilerplate)

        os.system("git clone https://github.com/Pr0gramm3rZ/" +
                  boilerName + ".git .")

        os.system("git remote set-url origin " + resp.json()["clone_url"])

        os.system('git push -u origin master')

        with open("package.json", "r") as jsonFile:
            data = json.load(jsonFile)

        data["name"] = projectName

        with open("package.json", "w") as jsonFile:
            json.dump(data, jsonFile)

        os.system('git add *')

        os.system('git commit -m "Name Updated"')

        os.system('git push -u origin master')

        os.system("npm install")

        os.system("code .")

else:
    print("Directory is not empty")
