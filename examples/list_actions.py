from dotenv import load_dotenv
from os.path import join, dirname
import sara_sdk
import itertools
import os

"""
This example shows how to list all actions of robots

We use dotenv to load the environment variables from the .env file
"""


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ACCESS_KEY = os.environ.get("ACCESS_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")

# Auth is necessary to generate access_token from access_key and secret_key
sara_sdk.auth(ACCESS_KEY, SECRET_KEY)

# This method returns a list with all services
services = sara_sdk.iam.services.list()

# This method returns a list with all actions
actions = sara_sdk.iam.actions.list()

for action in actions:
    action['service'] = next(s.get("name") for s in services if s.get("uuid") == action.get("service"))


for action in sorted(actions, key=lambda k: k['service']):
    print(action)    
    print("--------")