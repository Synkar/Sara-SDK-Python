from dotenv import load_dotenv
from os.path import join, dirname
import sara_sdk
import os
import itertools

"""
This example shows how to list all localities, operations and requests

We use dotenv to load the environment variables from the .env file
"""

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ACCESS_KEY = os.environ.get("ACCESS_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")

# Auth is necessary to generate access_token from access_key and secret_key
sara_sdk.auth(ACCESS_KEY, SECRET_KEY)

# This method returns a list with localities paginated
localities = sara_sdk.hivemind.localities.list_paginated()

for locality in list(itertools.chain.from_iterable(localities)):
    print(locality)
    print("--------")

# This method returns a list with operations paginated
operations = sara_sdk.hivemind.operations.list_paginated()

for operation in list(itertools.chain.from_iterable(operations)):
    print(operation)
    print("--------")

# This method returns a list with requests paginated
requests = sara_sdk.hivemind.requests.list_paginated()

for request in list(itertools.chain.from_iterable(requests)):
    print(request)
    print("--------")