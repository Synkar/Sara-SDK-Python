from sara_sdk.common.session import Session
from dotenv import load_dotenv
from sara_sdk import API_URL
import pytest
import os
import sara_sdk.core.webhook.topics as sara_sdk


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
        "limit": 10,
        "results": [
            {
                "service": "telemetry",
                "createdAt": "2022-09-12T21:38:49.895Z",
                "action": "RetrieveBattery",
                "name": "BatteryVoltage"
            }
        ]
    }
    requests_mock.get(f'{API_URL}v1/webhook/topics/?service=telemetry',
                      status_code=200, json=data)
    result = sara_sdk.list(session=default_session, service="telemetry")
    assert result == data


def test_create(default_session, requests_mock):
    data = {
        "service": "telemetry",
        "action": "RetrieveBattery",
        "name": "BatteryVoltage"
    }
    requests_mock.post(f'{API_URL}v1/webhook/topics/',
                       status_code=200, json=data)
    result = sara_sdk.create(
        name=data["name"], action=data["action"], service=data["service"], session=default_session)
    assert result == data


def test_delete(default_session, requests_mock):
    requests_mock.delete(f'{API_URL}v1/webhook/topics/telemetry/RetrieveBattery/',
                         status_code=204, json={'detail': 'Relation deleted successfully'})
    result = sara_sdk.delete(
        service="telemetry", action="RetrieveBattery", session=default_session)
    assert result['detail'] == 'Relation deleted successfully'
