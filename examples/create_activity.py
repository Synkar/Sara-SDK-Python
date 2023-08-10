from dotenv import load_dotenv
from os.path import join, dirname
import sara_sdk
import itertools
import os

"""
This example shows how to create a activity in srs

We use dotenv to load the environment variables from the .env file
"""


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ACCESS_KEY = os.environ.get("ACCESS_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")

# Auth is necessary to generate access_token from access_key and secret_key
sara_sdk.auth(ACCESS_KEY, SECRET_KEY)

sara_sdk.srs.activities.create(relationship="7fe05ab1-f8cb-44a3-8d6f-14bfd647eba3", type="U", robots=["0d9194fc-dc3a-4c75-af5d-0bd8537841ac"], files=["internet_info.json"])

