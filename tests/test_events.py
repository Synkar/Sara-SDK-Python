from sara_sdk.common.session import Session
from dotenv import load_dotenv
from sara_sdk import API_URL
import pytest
import os
import sara_sdk.core.webhook.events as sara_sdk


@pytest.fixture
def default_session():

    load_dotenv()
    ACCESS_KEY = os.getenv('ACCESS_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    new_session = Session(ACCESS_KEY, SECRET_KEY)
    new_session.auth()
    return new_session


def test_retrieve(default_session, requests_mock):
    data = {
        "createdAt": "2021-04-09T18:34:36.138Z",
        "id": "f57fd46a-2ead-471b-88ed-bc86d64d9901",
        "topic": "telemetry/RetrieveRobotPose",
        "robot": "f8b85a7a-4540-4d46-a2ed-00e6134ee84a",
        "data": "{\"orientation\":{\"w\":0.9468499913705694,\"z\":0.3216754464525686,\"y\":0,\"x\":0},\"z\":0,\"y\":-2.345813751220703,\"x\":-14.56182861328125}"
    }
    requests_mock.get(f'{API_URL}v1/webhook/events/f8b85a7a-4540-4d46-a2ed-00e6134ee84a/',
                      status_code=200, json=data)
    result = sara_sdk.retrieve(
        uuid="f8b85a7a-4540-4d46-a2ed-00e6134ee84a", session=default_session)
    assert result == data
