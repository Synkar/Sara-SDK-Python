from dotenv import load_dotenv
from os.path import join, dirname
import sara_sdk
import os

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

# This method returns a list with localities
localities = sara_sdk.hivemind.localities.list()

for locality in localities:
    print(locality)
    print(localities[locality])
    print("--------")
    
# This method returns a list with operations 
operations = sara_sdk.hivemind.operations.list()

for operation in operations:
    print(operation)
    print(operations[operation])
    print("--------")

# This method returns a list with requests
requests = sara_sdk.hivemind.requests.list()

for request in requests:
    print(request)
    print(requests[request])
    print("--------")
