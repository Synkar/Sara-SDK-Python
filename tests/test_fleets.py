from sara_sdk.common.session import Session
from dotenv import load_dotenv
import pytest
import os
import sara_sdk.core.iam.fleets as sara_sdk


@pytest.fixture
def default_session():

    load_dotenv()
    ACCESS_KEY = os.getenv('ACCESS_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    new_session = Session(ACCESS_KEY, SECRET_KEY)
    new_session.auth()
    return new_session


def test_fleets_list(default_session):
    result = sara_sdk.list(session=default_session, page=1, page_size=10)
    assert result["count"] >= 0


def test_fleets_retrieve(default_session):
    result = sara_sdk.retrieve(
        uuid="3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc", session=default_session)
    assert result["uuid"] == "3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc"


def test_fleets_update(default_session):
    model = {
        "name": "Test Fleet"
    }
    result = sara_sdk.update(
        uuid="3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc", model=model, session=default_session)
    assert result["name"] == "Test Fleet"
