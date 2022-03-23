from sara_sdk.common.session import Session
from dotenv import load_dotenv
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


def test_actions_list(default_session):
    result = sara_sdk.list(session=default_session, page=1, page_size=10)
    assert len(result) > 0


def test_actions_retrieve(default_session):
    result = sara_sdk.retrieve(
        uuid="3e8b4190-8d34-4299-bc52-4617e0711b70", session=default_session)
    assert result["uuid"] == "3e8b4190-8d34-4299-bc52-4617e0711b70"
