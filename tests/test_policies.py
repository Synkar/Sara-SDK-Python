from sara_sdk.common.session import Session
from dotenv import load_dotenv
import pytest
import os
import sara_sdk.core.iam.policies as sara_sdk

policy_created = ""


@pytest.fixture
def default_session():

    load_dotenv()
    ACCESS_KEY = os.getenv('ACCESS_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    new_session = Session(ACCESS_KEY, SECRET_KEY)
    new_session.auth()
    return new_session


def test_policies_create(default_session):
    model = {
        "name": "test policy",
        "description": "description test",
        "scope": 0,
        "resource": 0,
        "client": "f89356bd-294d-4f55-8395-c4825a296b95"
    }
    result = sara_sdk.create(model=model, session=default_session)
    global policy_created
    policy_created = result["uuid"]
    assert result["name"] == "test policy"


def test_policies_list(default_session):
    result = sara_sdk.list(session=default_session)
    assert len(result) > 0


def test_policies_retrieve(default_session):
    global policy_created
    result = sara_sdk.retrieve(
        uuid=policy_created, session=default_session)
    assert result["uuid"] == policy_created


def test_policies_delete(default_session):
    global policy_created
    result = sara_sdk.delete(uuid=policy_created, session=default_session)
    assert result == {}
