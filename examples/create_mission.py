from dotenv import load_dotenv
from os.path import join, dirname
import sara_sdk
import os
import time

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

# Robot UUID
robot = "144cdc28-9126-4f59-b32b-307b2ae43fb3"

# Stage with uuid and param_values
stages = [
    {
        "uuid": "0ae6df3c-1868-4729-988d-78c1b52984b6",  # Stage From Synkar-Client
        "param_values": [
            {
                "param": "8bf91997-b829-4d94-b7c3-4e29957aadf9",
                "step_value": "12"
            }
        ]
    }
]

# Create a mission
sara_sdk.missions.create(robot, stages)

# Print the mission datetime creation that was created above
print("Mission created at:", sara_sdk.missions.last(
    robot).get("datetime_created"))

try:
    while True:

        # Get the last mission by robot
        last_mission = sara_sdk.missions.last(robot)

        # Terminal status is 10, 11, 12, 13, 14, 15, 16
        if last_mission.get("status", -1) >= 10:
            print("Mission finished with status:", last_mission.get("status"))
            break
        else:
            print("Status:", last_mission.get("status"))
            print("Current step: ", last_mission.get("current_step"))
            print("------------------")
            time.sleep(5)
except KeyboardInterrupt:
    print("Script interrupted by user")
