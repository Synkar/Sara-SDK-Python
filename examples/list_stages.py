from dotenv import load_dotenv
from os.path import join, dirname
import sara_sdk
import itertools
import os

"""
This example shows how to list all stages of client with its variable params

We use dotenv to load the environment variables from the .env file
"""


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ACCESS_KEY = os.environ.get("ACCESS_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")

# Auth is necessary to generate access_token from access_key and secret_key
sara_sdk.auth(ACCESS_KEY, SECRET_KEY)

# This returns a iterator of all pages from listed stages
stages = sara_sdk.missions.stages.list_paginated()

# This interate of each stage in list of all stages from all pages
for stage in list(itertools.chain.from_iterable(stages)):
    # print stage name and stage uuid
    print("Name: {}".format(stage.get("name")))
    print("UUID: {}".format(stage.get("uuid")))
    print("")
    print("Variable Params:")

    has_variable_param = False

    for step in stage.get("steps", []):
        for param in step.get("params", []):
            if not param.get("is_variable", False):
                continue
            has_variable_param = True

            # print variable param name and variable param uuid
            print("  - Name: {}".format(param.get("name")))
            print("    UUID: {}".format(param.get("uuid")))
    if not has_variable_param:
        # if there is no variable param, print "No variable param"
        print("  No variable params")

    # print empty line
    print("------")
