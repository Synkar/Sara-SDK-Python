from dotenv import load_dotenv
from os.path import join, dirname
import sara_sdk
import os

"""
This example shows how to delete a locality, operation and request

We use dotenv to load the environment variables from the .env file
"""

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ACCESS_KEY = os.environ.get("ACCESS_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")

# Auth is necessary to generate access_token from access_key and secret_key
sara_sdk.auth(ACCESS_KEY, SECRET_KEY)

# This method deletes a locality by slug
locality = sara_sdk.hivemind.localities.delete("test_locality")

print(locality)

# This method deletes a operation by uuid
operation = sara_sdk.hivemind.operations.delete("64a27b0c-86de-49ae-9b14-ee4858372cd7")

print(operation)
