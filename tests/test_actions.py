from sara_sdk.common.session import Session
from dotenv import load_dotenv
from sara_sdk import API_URL
import pytest
import os
import sara_sdk.core.iam.actions as sara_sdk


@pytest.fixture
def default_session():

    load_dotenv()
    ACCESS_KEY = os.getenv('ACCESS_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    new_session = Session(ACCESS_KEY, SECRET_KEY)
    new_session.auth()
    return new_session


def test_actions_list(default_session, requests_mock):
    requests_mock.get(f'{API_URL}v1/iam/actions/?page=1&page_size=10',
                      status_code=200, json=[{'name': 'action_name'}])
    result = sara_sdk.list(session=default_session, page=1, page_size=10)
    assert result == [{'name': 'action_name'}]


def test_actions_retrieve(default_session, requests_mock):
    requests_mock.get(f'{API_URL}v1/iam/actions/3e8b4190-8d34-4299-bc52-4617e0711b70/',
                      status_code=200, json={'uuid': '3e8b4190-8d34-4299-bc52-4617e0711b70'})
    result = sara_sdk.retrieve(
        uuid="3e8b4190-8d34-4299-bc52-4617e0711b70", session=default_session)
    assert result["uuid"] == "3e8b4190-8d34-4299-bc52-4617e0711b70"


def test_actions_create(default_session, requests_mock):
    data = {'name': 'AttachRobot', 'type': 'A',
            'service': '7e5ebea3-955d-45b0-8c03-8a7f9de95e37'}
    requests_mock.post(f'{API_URL}v1/iam/actions/', status_code=201, json=data)
    result = sara_sdk.create(data, default_session)
    assert result == data
