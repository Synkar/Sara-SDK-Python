import json
from unittest import result
from sara_sdk.common.session import Session
from dotenv import load_dotenv
from sara_sdk import API_URL
import pytest
import os
import sara_sdk.core.missions.stages as sara_sdk


@pytest.fixture
def default_session():

    load_dotenv()
    ACCESS_KEY = os.getenv('ACCESS_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    new_session = Session(ACCESS_KEY, SECRET_KEY)
    new_session.auth()
    return new_session


def test_stages_list(default_session, requests_mock):
    data = [{
        'uuid': '3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc',
        'name': 'stage_name',
    }]
    requests_mock.get(f'{API_URL}v2/missions/stages/?page=1&page_size=10',
                      status_code=200, json=data)
    result = sara_sdk.list(session=default_session, page=1, page_size=10)
    assert result == data


def test_stages_retrieve(default_session, requests_mock):
    data = {
        'uuid': '3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc',
        'name': 'stage_name',
    }
    requests_mock.get(f'{API_URL}v2/missions/stages/3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc/',
                      status_code=200, json=data)
    result = sara_sdk.retrieve(
        uuid="3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc", session=default_session)
    assert result["uuid"] == "3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc"


def test_stages_list_paginated(default_session, requests_mock):
    data_page1 = {
        'next': 2,
        'count': 2,
        'previous': None,
        'results': [{
            "uuid": "4c8c04f0-88ec-4c6a-8041-8e90d366dbff",
            "name": "teste trava ifood",
            "description": "",
            "steps": []
        }]
    }
    data_page2 = {
        'next': None,
        'count': 2,
        'previous': 1,
        'results': [
            {
                "uuid": "a9d12c2f-03cf-44ab-bef7-d7c93235a9e2",
                "name": "teste",
                "description": "",
                "steps": []
            }]
    }
    requests_mock.get(f'{API_URL}v2/missions/stages/?page=1&page_size=1',
                      status_code=200, json=data_page1)
    requests_mock.get(f'{API_URL}v2/missions/stages/?page=2&page_size=1',
                      status_code=200, json=data_page2)
    result = sara_sdk.list_paginated(session=default_session, page_size=1)
    assert list(result) == [data_page1['results'], data_page2['results']]


def test_stages_update(default_session, requests_mock):
    data = {
        'uuid': '3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc',
        'name': 'stage_name',
    }
    requests_mock.patch(f'{API_URL}v2/missions/stages/3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc/',
                        status_code=200, json=data)
    result = sara_sdk.update(
        uuid="3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc", model=data, session=default_session)
    assert result == data


def test_stages_create(default_session, requests_mock):
    data = {
        'uuid': '3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc',
        'name': 'stage_name',
    }
    requests_mock.post(f'{API_URL}v2/missions/stages/',
                       status_code=200, json=data)
    result = sara_sdk.create(model=data, session=default_session)
    assert result == data


def test_stages_delete(default_session, requests_mock):
    requests_mock.delete(f'{API_URL}v2/missions/stages/3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc/',
                         status_code=204, json={'detail': 'Stage deleted successfully'})
    result = sara_sdk.delete(
        uuid="3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc", session=default_session)
    assert result['detail'] == 'Stage deleted successfully'


def test_list_steps(default_session, requests_mock):
    data = {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [
            {
                "uuid": "73b90897-dbb0-4480-b6d0-1cc359fc3841",
                "name": "Abrir trava",
            }
        ]
    }
    requests_mock.get(f'{API_URL}v2/missions/stages/3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc/steps/',
                      status_code=200, json=data)
    result = sara_sdk.list_steps(
        stage="3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc", session=default_session)
    assert result == data


def test_retrieve_step(default_session, requests_mock):
    data = {
        "uuid": "73b90897-dbb0-4480-b6d0-1cc359fc3841",
        "name": "Abrir trava",
    }
    requests_mock.get(f'{API_URL}v2/missions/stages/3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc/steps/73b90897-dbb0-4480-b6d0-1cc359fc3841/',
                      status_code=200, json=data)
    result = sara_sdk.retrieve_steps(
        stage="3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc", step="73b90897-dbb0-4480-b6d0-1cc359fc3841", session=default_session)
    assert result == data


def test_list_params(default_session, requests_mock):
    data = {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [
            {
                "uuid": "73b90897-dbb0-4480-b6d0-1cc359fc3841",
                "name": "Landmark identifier",
            }
        ]
    }
    requests_mock.get(f'{API_URL}v2/missions/stages/3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc/params/',
                      status_code=200, json=data)
    result = sara_sdk.list_params(
        stage="3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc", session=default_session)
    assert result == data


def test_retrieve_params(default_session, requests_mock):
    data = {
        "uuid": "73b90897-dbb0-4480-b6d0-1cc359fc3841",
        "name": "Landmark identifier",
    }
    requests_mock.get(f'{API_URL}v2/missions/stages/3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc/params/73b90897-dbb0-4480-b6d0-1cc359fc3841/',
                      status_code=200, json=data)
    result = sara_sdk.retrieve_params(
        stage="3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc", param="73b90897-dbb0-4480-b6d0-1cc359fc3841", session=default_session)
    assert result == data
