from sara_sdk.common.session import Session
from dotenv import load_dotenv
from sara_sdk import API_URL
import pytest
import os
import sara_sdk.core.iam.robots as sara_sdk


@pytest.fixture
def default_session():

    load_dotenv()
    ACCESS_KEY = os.getenv('ACCESS_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    new_session = Session(ACCESS_KEY, SECRET_KEY)
    new_session.auth()
    return new_session


def test_robots_listing(default_session, requests_mock):
    data = [{
        "uuid": "f8b85a7a-4540-4d46-a2ed-00e6134ee84a",
        "name": "test robot",
        "description": "description test",
        "client": "f89356bd-294d-4f55-8395-c4825a296b95"
    }]
    requests_mock.get(f'{API_URL}v1/iam/robots/?page=1&page_size=10',
                      status_code=200, json=data)
    result = sara_sdk.list(session=default_session, page=1, page_size=10)
    assert result == data


def test_robots_retrieve(default_session, requests_mock):
    data = {
        "uuid": "f8b85a7a-4540-4d46-a2ed-00e6134ee84a",
        "name": "test robot",
        "description": "description test",
        "client": "f89356bd-294d-4f55-8395-c4825a296b95"
    }
    requests_mock.get(f'{API_URL}v1/iam/robots/f8b85a7a-4540-4d46-a2ed-00e6134ee84a/',
                      status_code=200, json=data)
    result = sara_sdk.retrieve(
        uuid="f8b85a7a-4540-4d46-a2ed-00e6134ee84a", session=default_session)
    assert result == data


def test_robots_update(default_session, requests_mock):
    model = {
        "uuid": "f8b85a7a-4540-4d46-a2ed-00e6134ee84a",
        "name": "test robot",
        "description": "description test",
        "client": "f89356bd-294d-4f55-8395-c4825a296b95"
    }
    requests_mock.patch(f'{API_URL}v1/iam/robots/f8b85a7a-4540-4d46-a2ed-00e6134ee84a/',
                        status_code=200, json=model)
    result = sara_sdk.update(
        uuid="f8b85a7a-4540-4d46-a2ed-00e6134ee84a", model=model, session=default_session)
    assert result == model


def test_robots_delete(default_session, requests_mock):
    requests_mock.delete(f'{API_URL}v1/iam/robots/f8b85a7a-4540-4d46-a2ed-00e6134ee84a/',
                         status_code=200, json={'detail': 'Robot deleted successfully'})
    result = sara_sdk.delete(
        uuid="f8b85a7a-4540-4d46-a2ed-00e6134ee84a", session=default_session)
    assert result['detail'] == 'Robot deleted successfully'
