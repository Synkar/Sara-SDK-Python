import json
from unittest import result
from sara_sdk.common.session import Session
from dotenv import load_dotenv
from sara_sdk import API_URL
import pytest
import os
import sara_sdk.core.missions.steps as sara_sdk

@pytest.fixture
def default_session():

    load_dotenv()
    ACCESS_KEY = os.getenv('ACCESS_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    new_session = Session(ACCESS_KEY, SECRET_KEY)
    new_session.auth()
    return new_session

def test_steps_list(default_session, requests_mock):
    data = [{
        'uuid': '3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc',
        'name': 'step_name',
    }]
    requests_mock.get(f'{API_URL}v2/missions/steps/?page=1&page_size=10',
                      status_code=200, json=data)
    result = sara_sdk.list(session=default_session, page=1, page_size=10)
    assert result == data

def test_steps_retrieve(default_session, requests_mock):
    data = {
        'uuid': '3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc',
        'name': 'step_name',
    }
    requests_mock.get(f'{API_URL}v2/missions/steps/3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc/',
                      status_code=200, json=data)
    result = sara_sdk.retrieve(
        uuid="3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc", session=default_session)
    assert result["uuid"] == "3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc"

def test_steps_list_paginated(default_session, requests_mock):
    data_page1 = {
        'next': 2,
        'count': 2,
        'previous': None,
        'results': [{
            "uuid": "73b90897-dbb0-4480-b6d0-1cc359fc3841",
            "name": "Abrir trava",
            "robot_type": "SD02",
            "description": "",
            "datetime_created": "2022-07-13T20:06:29.401543Z",
            "datetime_updated": "2022-07-13T20:06:29.401562Z",
            "active": True},
        ]
    }
    data_page2 = {
        'next': None,
        'count': 2,
        'previous': 1,
        'results': [
            {
            "uuid": "29c82f02-7b10-4044-8b4d-7f51b0970112",
            "name": "Go To Landmark",
            "robot_type": "SD02",
            "description": "",
            "datetime_created": "2022-07-07T18:47:11.986049Z",
            "datetime_updated": "2022-07-07T18:47:11.986069Z",
            "active": True
        }]
    }
    requests_mock.get(f'{API_URL}v2/missions/steps/?page=1&page_size=1',
                      status_code=200, json=data_page1)
    requests_mock.get(f'{API_URL}v2/missions/steps/?page=2&page_size=1',
                      status_code=200, json=data_page2)
    result = sara_sdk.list_paginated(session=default_session, page_size=1)
    assert list(result) == [data_page1['results'], data_page2['results']]

def test_steps_update(default_session, requests_mock):
    data = {
        'uuid': '3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc',
        'name': 'step_name',
    }
    requests_mock.patch(f'{API_URL}v2/missions/steps/3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc/',
                      status_code=200, json=data)
    result = sara_sdk.update(
        uuid="3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc", model=data, session=default_session)
    assert result == data

def test_steps_create(default_session, requests_mock):
    data = {
        'name': 'step_name',
    }
    requests_mock.post(f'{API_URL}v2/missions/steps/',
                       status_code=200, json=data)
    result = sara_sdk.create(model=data, session=default_session)
    assert result == data

def test_steps_delete(default_session, requests_mock):
    requests_mock.delete(f'{API_URL}v2/missions/steps/3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc/',
                         status_code=200, json={'detail': 'Stage deleted successfully'})
    result = sara_sdk.delete(
        uuid="3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc", session=default_session)
    assert result['detail'] == 'Stage deleted successfully'