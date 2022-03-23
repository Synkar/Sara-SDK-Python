from sara_sdk.common.session import Session
from dotenv import load_dotenv
import pytest
import os
import sara_sdk.core.iam.users as sara_sdk

user_created = ""


@pytest.fixture
def default_session():

    load_dotenv()
    ACCESS_KEY = os.getenv('ACCESS_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    new_session = Session(ACCESS_KEY, SECRET_KEY)
    new_session.auth()
    return new_session


def test_users_create(default_session):
    model = {
        "email": "test@test.com",
        "username": "test-user-sdk",
        "first_name": "Test",
        "last_name": "User",
        "is_staff": False
    }
    result = sara_sdk.create(model=model, session=default_session)
    global user_created
    user_created = result["uuid"]
    assert result["username"] == "test-user-sdk"


def test_users_list(default_session):
    result = sara_sdk.list(session=default_session)
    assert len(result) > 0


def test_users_retrieve(default_session):
    global user_created
    result = sara_sdk.retrieve(
        uuid=user_created, session=default_session)
    assert result["uuid"] == user_created


def test_users_delete(default_session):
    global user_created
    result = sara_sdk.delete(uuid=user_created, session=default_session)
    assert result == {}
