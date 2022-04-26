from sara_sdk.common.session import Session
from dotenv import load_dotenv
from sara_sdk import API_URL
import pytest
import os
import sara_sdk.core.iam.services as sara_sdk


@pytest.fixture
def default_session():

    load_dotenv()
    ACCESS_KEY = os.getenv('ACCESS_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    new_session = Session(ACCESS_KEY, SECRET_KEY)
    new_session.auth()
    return new_session


def test_services_list(default_session, requests_mock):
    data = [{
        "uuid": "f8b85a7a-4540-4d46-a2ed-00e6134ee84a",
        "name": "service name",
        "description": "description test",
        "client": "f89356bd-294d-4f55-8395-c4825a296b95"
    }]
    requests_mock.get(f'{API_URL}v1/iam/services/',
                      status_code=200, json=data)
    result = sara_sdk.list(session=default_session)
    assert result == data


def test_services_retrieve(default_session, requests_mock):
    data = {
        "uuid": "f8b85a7a-4540-4d46-a2ed-00e6134ee84a",
        "name": "service name",
        "description": "description test",
        "client": "f89356bd-294d-4f55-8395-c4825a296b95"
    }
    requests_mock.get(f'{API_URL}v1/iam/services/250720c8-d001-4c98-b5c6-0476dc424a3b/',
                      status_code=200, json=data)
    result = sara_sdk.retrieve(
        uuid="250720c8-d001-4c98-b5c6-0476dc424a3b", session=default_session)
    assert result == data


def test_services_create(default_session, requests_mock):
    data = {
        "uuid": "f8b85a7a-4540-4d46-a2ed-00e6134ee84a",
        "name": "service name",
        "description": "description test",
        "client": "f89356bd-294d-4f55-8395-c4825a296b95"
    }
    requests_mock.post(f'{API_URL}v1/iam/services/',
                       status_code=200, json=data)
    result = sara_sdk.create(
        model=data, session=default_session)
    assert result == data
