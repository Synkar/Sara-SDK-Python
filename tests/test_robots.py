from sara_sdk.common.session import Session
from dotenv import load_dotenv
import pytest
import os
import sara_sdk.core.iam.robots as sara_sdk
import json


@pytest.fixture
def default_session():

    load_dotenv()
    ACCESS_KEY = os.getenv('ACCESS_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    new_session = Session(ACCESS_KEY, SECRET_KEY)
    new_session.auth()
    return new_session


def test_listing_robots(default_session):
    result = sara_sdk.list(session=default_session, page=1, page_size=10)
    print(result)
    assert result["count"] >= 0


def test_retrieve_robot(default_session: Session):
    result = sara_sdk.retrieve(
        uuid="f8b85a7a-4540-4d46-a2ed-00e6134ee84a", session=default_session)
    assert result["uuid"] == "f8b85a7a-4540-4d46-a2ed-00e6134ee84a"


def test_update_robot(default_session: Session):
    model = {
        "name": "Test Robot"
    }
    result = sara_sdk.update(
        uuid="f8b85a7a-4540-4d46-a2ed-00e6134ee84a", model=model, session=default_session)
    assert result["name"] == "Test Robot"
