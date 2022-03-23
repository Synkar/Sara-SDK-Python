from sara_sdk.common.session import Session
from dotenv import load_dotenv
import pytest
import os
import sara_sdk.core.iam.apps as sara_sdk

app_created = ""


@pytest.fixture
def default_session():

    load_dotenv()
    ACCESS_KEY = os.getenv('ACCESS_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    new_session = Session(ACCESS_KEY, SECRET_KEY)
    new_session.auth()
    return new_session


def test_apps_create(default_session):
    model = {
        "name": "test_app",
        "description": "description"
    }
    result = sara_sdk.create(model=model, session=default_session)
    global app_created
    app_created = result["id"]
    assert result["name"] == "test_app"


def test_apps_list(default_session):
    result = sara_sdk.list(session=default_session)
    assert len(result) > 0


def test_apps_retrieve(default_session):
    global app_created
    result = sara_sdk.retrieve(
        id=app_created, session=default_session)
    assert result["id"] == app_created


def test_apps_delete(default_session):
    global app_created
    result = sara_sdk.delete(id=app_created, session=default_session)
    assert result == {}
