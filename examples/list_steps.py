from dotenv import load_dotenv
from os.path import join, dirname
import sara_sdk
import itertools
import os

"""
This example shows how to list all steps of robots

We use dotenv to load the environment variables from the .env file
"""


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ACCESS_KEY = os.environ.get("ACCESS_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")

# Auth is necessary to generate access_token from access_key and secret_key
sara_sdk.auth(ACCESS_KEY, SECRET_KEY)

# This method return a iterator of all pages from listed steps
steps = sara_sdk.missions.steps.list_paginated()

# This interate of each step in list of all steps from all pages
for step in list(itertools.chain.from_iterable(steps)):
    print("- Name: {}".format(step.get("name")))
    print("  UUID: {}".format(step.get("uuid")))
    print("--------")
