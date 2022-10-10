from sara_sdk.common.session import Session
from dotenv import load_dotenv
from sara_sdk import API_URL
import pytest
import os
import sara_sdk.core.webhook.events_execution as sara_sdk


@pytest.fixture
def default_session():

    load_dotenv()
    ACCESS_KEY = os.getenv('ACCESS_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    new_session = Session(ACCESS_KEY, SECRET_KEY)
    new_session.auth()
    return new_session


def test_list(default_session, requests_mock):
    data = {
        "count": 1,
        "limit": 30,
        "nextToken": "eyJlbmRwb2ludCI6ImQzOWZlYTI2LTBjNTktNDgzNS1hMDU5LWFhZjZjYjEyZDc4MiIsImNyZWF0ZWRBdCI6MTYyMzg3NTc0MDg5N30=",
        "results": [
            {
                "eventId": "f1b1f769-e9e7-4497-90d1-5518c46f17a2",
                "topic": "telemetry/RetrieveRobotPose",
                "statusCode": 104,
                "robot": "f8b85a7a-4540-4d46-a2ed-00e6134ee84a",
                "response": "Tunnel c89209b737b4.ngrok.io not found",
                "createdAt": "2021-06-16T20:36:40.450Z",
                "id": "85f81a85-f98d-476e-9a71-e42c2f7a6d10",
                "endpoint": "d39fea26-0c59-4835-a059-aaf6cb12d782"
            }
        ]
    }
    requests_mock.get(f'{API_URL}v1/webhook/event-executions/?endpoint=d39fea26-0c59-4835-a059-aaf6cb12d782',
                      status_code=200, json=data)
    result = sara_sdk.list(session=default_session,
                           endpoint="d39fea26-0c59-4835-a059-aaf6cb12d782")
    assert result == data
