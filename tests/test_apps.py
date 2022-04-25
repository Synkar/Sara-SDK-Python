from sara_sdk.common.session import Session
from dotenv import load_dotenv
from sara_sdk import API_URL
import pytest
import os
import sara_sdk.core.iam.apps as sara_sdk


@pytest.fixture
def default_session():

    load_dotenv()
    ACCESS_KEY = os.getenv('ACCESS_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    new_session = Session(ACCESS_KEY, SECRET_KEY)
    new_session.auth()
    return new_session


def test_apps_create(default_session, requests_mock):
    model = {
        "name": "test_app",
        "description": "description"
    }
    requests_mock.post(f'{API_URL}v1/iam/apps/', status_code=201, json=model)
    result = sara_sdk.create(model=model, session=default_session)
    assert result == model


def test_apps_list(default_session, requests_mock):
    requests_mock.get(f'{API_URL}v1/iam/apps/',
                      status_code=200, json=[{'name': 'app_name'}])
    result = sara_sdk.list(session=default_session)
    assert result == [{'name': 'app_name'}]


def test_apps_retrieve(default_session, requests_mock):
    requests_mock.get(f'{API_URL}v1/iam/apps/51qoapqvprat87o7jkqd1beae9/',
                      status_code=200, json={'name': 'app_name', 'id': '51qoapqvprat87o7jkqd1beae9'})
    result = sara_sdk.retrieve(
        id="51qoapqvprat87o7jkqd1beae9", session=default_session)
    assert result["id"] == '51qoapqvprat87o7jkqd1beae9'


def test_apps_delete(default_session, requests_mock):
    requests_mock.delete(f'{API_URL}v1/iam/apps/51qoapqvprat87o7jkqd1beae9/',
                         status_code=200, json={'name': 'app_name', 'id': '51qoapqvprat87o7jkqd1beae9'})
    result = sara_sdk.delete(
        id='51qoapqvprat87o7jkqd1beae9', session=default_session)
    assert result["id"] == '51qoapqvprat87o7jkqd1beae9'
