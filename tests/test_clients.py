from sara_sdk.common.session import Session
from dotenv import load_dotenv
from sara_sdk.error import UnknownError
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


def test_clients_list(default_session):
    with pytest.raises(UnknownError):
        sara_sdk.list(session=default_session)


def test_clients_slugs(default_session):
    result = sara_sdk.slug("test-client", session=default_session)
    assert result["slug"] == "test-client"
