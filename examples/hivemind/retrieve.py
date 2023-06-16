from dotenv import load_dotenv
from os.path import join, dirname
import sara_sdk
import os

"""
This example shows how to retrieve a locality, operation and request

We use dotenv to load the environment variables from the .env file
"""

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ACCESS_KEY = os.environ.get("ACCESS_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")

# Auth is necessary to generate access_token from access_key and secret_key
sara_sdk.auth(ACCESS_KEY, SECRET_KEY)

# This method returns a locality by slug
locality = sara_sdk.hivemind.localities.retrieve("test_locality")

print(locality)

# This method returns a operation by uuid
operation = sara_sdk.hivemind.operations.retrieve("64a27b0c-86de-49ae-9b14-ee4858372cd7")

print(operation)

# This method returns a request by uuid
request = sara_sdk.hivemind.requests.retrieve("5538c856-b58a-4603-a01d-c545c71e788c")

print(request)
