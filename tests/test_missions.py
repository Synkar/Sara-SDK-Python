import json
from unittest import result
from sara_sdk.common.session import Session
from dotenv import load_dotenv
from sara_sdk import API_URL
import pytest
import os
import sara_sdk.core.missions as sara_sdk

@pytest.fixture
def default_session():

    load_dotenv()
    ACCESS_KEY = os.getenv('ACCESS_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    new_session = Session(ACCESS_KEY, SECRET_KEY)
    new_session.auth()
    return new_session

def test_missions_list(default_session, requests_mock):
    data = [{
        'uuid': 'mission_uuid',
        'robot': '3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc',
    }]
    requests_mock.get(f'{API_URL}v2/missions/?robot_id=3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc&page=1&page_size=10',
                      status_code=200, json=data)
    result = sara_sdk.list(robot="3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc",session=default_session, page=1, page_size=10)
    assert result == data


def test_missions_retrieve(default_session, requests_mock):
    data = {
        'uuid': '3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc',
        'robot': '3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc',
    }
    requests_mock.get(f'{API_URL}v2/missions/3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc/',
                      status_code=200, json=data)
    result = sara_sdk.retrieve(
        uuid="3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc", session=default_session)
    assert result["uuid"] == "3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc"

def test_missions_list_paginated(default_session, requests_mock):
    data_page1 = {
        'next': 2,
        'count': 2,
        'previous': None,
        'results': [{
            "uuid": "a56356c3-ca70-413f-8561-26f09cd6f488",
            "robot": "eebed4ca-fa3f-41a6-b826-3285c62762da",
            "current_step": 0,
            "status": -1,
            "assisted": False,
            "loop": False,
            "outcome": 0,
            "tags": [],
            "datetime_created": "2022-09-26T17:19:04.915796Z",
            "datetime_updated": "2022-09-26T17:19:04.933592Z"
        }]
    }
    data_page2 = {
        'next': None,
        'count': 2,
        'previous': 1,
        'results': [
            {
            "uuid": "a56356c3-ca70-413f-8561-26f09cd6f488",
            "robot": "eebed4ca-fa3f-41a6-b826-3285c62762da",
            "current_step": 0,
            "status": -1,
            "assisted": False,
            "loop": False,
            "outcome": 0,
            "tags": [],
            "datetime_created": "2022-09-26T17:19:04.915796Z",
            "datetime_updated": "2022-09-26T17:19:04.933592Z"
        }]
    }
    requests_mock.get(f'{API_URL}v2/missions/?page=1&page_size=1',
                      status_code=200, json=data_page1)
    requests_mock.get(f'{API_URL}v2/missions/?page=2&page_size=1',
                      status_code=200, json=data_page2)
    result = sara_sdk.list_paginated(robot="3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc",
        session=default_session, page_size=1)
    assert list(result) == [data_page1['results'], data_page2['results']]

def test_missions_last(default_session, requests_mock):
    data = [{
        'uuid': 'mission_uuid',
        'robot': '3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc',
    }]
    requests_mock.get(f'{API_URL}v2/missions/last/',
                      status_code=200, json=data)
    result = sara_sdk.last(robot="3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc",session=default_session)
    assert result == data

def test_missions_create(default_session, requests_mock):
    data = [{
        'robot': '3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc',
        'stages': [],
    }]
    requests_mock.post(f'{API_URL}v2/missions/',status_code=200, json=data)
    result = sara_sdk.create(robot="3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc",stages=[],session=default_session)
    assert result == data

def test_mission_retry(default_session, requests_mock):
    data = [{
        'mission': '3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc'
    }]
    requests_mock.post(f'{API_URL}v2/missions/3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc/retry/',status_code=202, json=data)
    result = sara_sdk.retry(mission="3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc",session=default_session)
    assert result == True

def test_mission_cancel(default_session, requests_mock):
    data = [{
        'mission': '3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc'
    }]
    requests_mock.post(f'{API_URL}v2/missions/3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc/cancel/',status_code=202, json=data)
    result = sara_sdk.cancel(mission="3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc",session=default_session)
    assert result == True

def test_mission_pause(default_session, requests_mock):
    data = [{
        'mission': '3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc'
    }]
    requests_mock.post(f'{API_URL}v2/missions/3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc/pause/',status_code=202, json=data)
    result = sara_sdk.pause(mission="3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc",session=default_session)
    assert result == True

def test_mission_resume(default_session, requests_mock):
    data = [{
        'mission': '3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc'
    }]
    requests_mock.post(f'{API_URL}v2/missions/3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc/resume/',status_code=202, json=data)
    result = sara_sdk.resume(mission="3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc",session=default_session)
    assert result == True