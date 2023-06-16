from dotenv import load_dotenv
from os.path import join, dirname
import sara_sdk
import os

"""
This example shows how to create a new locality, operation and request

We use dotenv to load the environment variables from the .env file
"""

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ACCESS_KEY = os.environ.get("ACCESS_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")

# Auth is necessary to generate access_token from access_key and secret_key
sara_sdk.auth(ACCESS_KEY, SECRET_KEY)

# This method creates a new locality
locality = sara_sdk.hivemind.localities.create({
    "slug": "test_locality",
    "robotCapacity": 1,
    "timestamps": [
      [
        60,
        73,
        106,
      ],
      [
        73,
        60,
        106
      ]
    ],
    "landmarks": [
      6,
      7,
      8,
    ],
    "depotLandmark": 6,
})

print(locality)

# This method creates a new operation
operation = sara_sdk.hivemind.operations.create({
  "locality": locality["slug"],
  "pickupMissionStage": "84cafed6-463b-4bd0-8261-500abde4c234",
  "deliveryMissionStage": "84cafed6-463b-4bd0-8261-500abde4c234",
  "pickupMissionStageLandmarkKey": "6873ad40-5212-442a-8110-0ffc540a8a9b",
  "deliveryMissionStageLandmarkKey": "6873ad40-5212-442a-8110-0ffc540a8a9b",
  "name": "test_operation",
  "description": "Test Operation",
})

print(operation)

# This method creates a new request
request = sara_sdk.hivemind.requests.create({
  "operation": operation["uuid"],
  "pickup": {
    "params": {
      "6873ad40-5212-442a-8110-0ffc540a8a9b": 7,
    },
    "windowTime": [
      0,
      9999
    ]
  },
  "delivery": {
    "params": {
      "6873ad40-5212-442a-8110-0ffc540a8a9b": 8,
    },
    "windowTime": [
      0,
      9999
    ]
  },
})

print(request)