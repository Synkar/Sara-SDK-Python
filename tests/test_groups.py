from sara_sdk.common.session import Session
from dotenv import load_dotenv
import pytest
import os
import sara_sdk.core.iam.groups as sara_sdk


@pytest.fixture
def default_session():

    load_dotenv()
    ACCESS_KEY = os.getenv('ACCESS_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    new_session = Session(ACCESS_KEY, SECRET_KEY)
    new_session.auth()
    return new_session


def test_groups_list(default_session):
    result = sara_sdk.list(session=default_session, page=1, page_size=10)
    assert result["count"] >= 0


def test_groups_retrieve(default_session):
    result = sara_sdk.retrieve(
        uuid="00ea03f1-5b2e-4787-8aa6-745961c6d506", session=default_session)
    assert result["uuid"] == "00ea03f1-5b2e-4787-8aa6-745961c6d506"


def test_groups_update(default_session):
    model = {
        "name": "Teste Group"
    }
    result = sara_sdk.update(
        uuid="00ea03f1-5b2e-4787-8aa6-745961c6d506", model=model, session=default_session)
    assert result["name"] == "Teste Group"
