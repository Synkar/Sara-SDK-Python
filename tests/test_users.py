from sara_sdk.common.session import Session
from dotenv import load_dotenv
from sara_sdk import API_URL
import pytest
import os
import sara_sdk.core.iam.users as sara_sdk


@pytest.fixture
def default_session():

    load_dotenv()
    ACCESS_KEY = os.getenv('ACCESS_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    new_session = Session(ACCESS_KEY, SECRET_KEY)
    new_session.auth()
    return new_session


def test_users_create(default_session, requests_mock):
    model = {
        "email": "test@test.com",
        "username": "test-user-sdk",
        "first_name": "Test",
        "last_name": "User"
    }
    requests_mock.post(f'{API_URL}v1/iam/users/',
                       status_code=200, json=model)
    result = sara_sdk.create(model=model, session=default_session)
    assert result == model


def test_users_list(default_session, requests_mock):
    model = [{
        "email": "test@test.com",
        "username": "test-user-sdk",
        "first_name": "Test",
        "last_name": "User"
    }]
    requests_mock.get(f'{API_URL}v1/iam/users/',
                      status_code=200, json=model)
    result = sara_sdk.list(session=default_session)
    assert result == model


def test_users_retrieve(default_session, requests_mock):
    model = {
        "uuid": "90d9c97e-c05d-4556-a625-9bdb9c588013",
        "email": "test@test.com",
        "username": "test-user-sdk",
        "first_name": "Test",
        "last_name": "User"
    }
    requests_mock.get(f'{API_URL}v1/iam/users/90d9c97e-c05d-4556-a625-9bdb9c588013/',
                      status_code=200, json=model)
    result = sara_sdk.retrieve(
        uuid='90d9c97e-c05d-4556-a625-9bdb9c588013', session=default_session)
    assert result == model


def test_users_delete(default_session, requests_mock):
    requests_mock.delete(f'{API_URL}v1/iam/users/90d9c97e-c05d-4556-a625-9bdb9c588013/',
                         status_code=200, json={'detail': 'User deleted successfully'})
    result = sara_sdk.delete(
        uuid="90d9c97e-c05d-4556-a625-9bdb9c588013", session=default_session)
    assert result['detail'] == 'User deleted successfully'


def test_users_update(default_session, requests_mock):
    model = {
        "uuid": "90d9c97e-c05d-4556-a625-9bdb9c588013",
        "email": "test@test.com",
        "username": "test-user-sdk",
        "first_name": "Test",
        "last_name": "User"
    }
    requests_mock.patch(f'{API_URL}v1/iam/users/90d9c97e-c05d-4556-a625-9bdb9c588013/',
                        status_code=200, json=model)
    result = sara_sdk.update(
        uuid="90d9c97e-c05d-4556-a625-9bdb9c588013", model=model, session=default_session)
    assert result == model


def test_users_me(default_session, requests_mock):
    model = {
        "uuid": "90d9c97e-c05d-4556-a625-9bdb9c588013",
        "email": "test@test.com",
        "username": "test-user-sdk",
        "first_name": "Test",
        "last_name": "User"
    }
    requests_mock.get(f'{API_URL}v1/iam/users/me/',
                      status_code=200, json=model)
    result = sara_sdk.me(session=default_session)
    assert result == model


def test_users_verify_user_by_email(default_session, requests_mock):
    requests_mock.get(f'{API_URL}v1/iam/users/verifyUserByEmail/',
                      status_code=200, json={'detail': 'User Email verified successfully'})
    result = sara_sdk.verifyUserByEmail(
        email="mail@teste.com", session=default_session)
    assert result['detail'] == 'User Email verified successfully'
