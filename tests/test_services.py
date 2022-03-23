from sara_sdk.common.session import Session
from dotenv import load_dotenv
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


def test_services_list(default_session):
    result = sara_sdk.list(session=default_session)
    assert len(result) >= 0


def test_services_retrieve(default_session: Session):
    result = sara_sdk.retrieve(
        uuid="250720c8-d001-4c98-b5c6-0476dc424a3b", session=default_session)
    assert result["uuid"] == "250720c8-d001-4c98-b5c6-0476dc424a3b"
