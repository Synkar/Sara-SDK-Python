from sara_sdk.common.session import Session
from dotenv import load_dotenv
from sara_sdk import API_URL
import pytest
import os
import sara_sdk.core.iam.clients as sara_sdk


@pytest.fixture
def default_session():

    load_dotenv()
    ACCESS_KEY = os.getenv('ACCESS_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    new_session = Session(ACCESS_KEY, SECRET_KEY)
    new_session.auth()
    return new_session


def test_clients_list(default_session, requests_mock):
    data = [{'name': 'client_name'}]
    requests_mock.get(f'{API_URL}v1/iam/clients/',
                      status_code=200, json=data)
    result = sara_sdk.list(session=default_session)
    assert result == data


def test_clients_slugs(default_session, requests_mock):
    requests_mock.get(f'{API_URL}v1/iam/slugs/',
                      status_code=200, json={'slug': 'test-client'})
    result = sara_sdk.slug("test-client", session=default_session)
    assert result["slug"] == "test-client"


def test_clients_attach_robot(default_session, requests_mock):
    requests_mock.post(f'{API_URL}v1/iam/clients/attachRobot/',
                       status_code=200, json={'detail': 'Robot attached successfully'})
    result = sara_sdk.attachRobot("2d1cb23c-181c-4c28-b078-9574ea84ff18",
                                  "cba10317-cfb0-465e-9f7f-8a3a51bf8cac", default_session)

    assert result["detail"] == "Robot attached successfully"


def test_clients_detach_robot(default_session, requests_mock):
    requests_mock.delete(f'{API_URL}v1/iam/clients/attachRobot/',
                         status_code=200, json={'detail': 'Robot detached successfully'})
    result = sara_sdk.detachRobot("2d1cb23c-181c-4c28-b078-9574ea84ff18",
                                  "cba10317-cfb0-465e-9f7f-8a3a51bf8cac", default_session)

    assert result["detail"] == "Robot detached successfully"


def test_clients_attach_user(default_session, requests_mock):
    requests_mock.post(f'{API_URL}v1/iam/clients/attachUser/',
                       status_code=200, json={'detail': 'User attached successfully'})
    result = sara_sdk.attachUser("2d1cb23c-181c-4c28-b078-9574ea84ff18",
                                 "cba10317-cfb0-465e-9f7f-8a3a51bf8cac", default_session)

    assert result["detail"] == "User attached successfully"


def test_clients_detach_user(default_session, requests_mock):
    requests_mock.delete(f'{API_URL}v1/iam/clients/attachUser/',
                         status_code=200, json={'detail': 'User detached successfully'})
    result = sara_sdk.detachUser("2d1cb23c-181c-4c28-b078-9574ea84ff18",
                                 "cba10317-cfb0-465e-9f7f-8a3a51bf8cac", default_session)

    assert result["detail"] == "User detached successfully"
