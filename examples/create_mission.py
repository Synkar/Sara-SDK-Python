from dotenv import load_dotenv
from os.path import join, dirname
import sara_sdk
import itertools
import os

"""
This example shows how create a mission with a list of stages and its variable params

We use dotenv to load the environment variables from the .env file
"""


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ACCESS_KEY = os.environ.get("ACCESS_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")

# Auth is necessary to generate access_token from access_key and secret_key
sara_sdk.auth(ACCESS_KEY, SECRET_KEY)
