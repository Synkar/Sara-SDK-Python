from sara_sdk.common.session import Session
from dotenv import load_dotenv
from sara_sdk import API_URL
import pytest
import os
import sara_sdk.core.webhook.endpoints as sara_sdk


@pytest.fixture
def default_session():

    load_dotenv()
    ACCESS_KEY = os.getenv('ACCESS_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    new_session = Session(ACCESS_KEY, SECRET_KEY)
    new_session.auth()
    return new_session


def test_list(default_session, requests_mock):
    data = {"count": 1,
            "limit": 10,
            "results": [
                {
                    "client": "308u5hheg50jhv65qorf95j3bq",
                    "updatedAt": "2021-07-26T12:25:19.258Z",
                    "createdAt": "2021-06-25T11:58:44.921Z",
                    "url": "https://teste/",
                    "id": "9263e695-c333-4d26-b278-10e59e57df65"
                }]
            }
    requests_mock.get(f'{API_URL}v1/webhook/endpoints/',
                      status_code=200, json=data)
    result = sara_sdk.list(session=default_session, page=1, page_size=10)
    assert result == data


def test_create(default_session, requests_mock):
    model = {
        "url": "https://teste/"
    }
    requests_mock.post(f'{API_URL}v1/webhook/endpoints/',
                       status_code=200, json=model)
    result = sara_sdk.create(url=model, session=default_session)
    assert result == model


def test_retrieve(default_session, requests_mock):
    data = {
        "client": "308u5hheg50jhv65qorf95j3bq",
        "updatedAt": "2021-07-26T12:25:19.258Z",
        "createdAt": "2021-06-25T11:58:44.921Z",
        "url": "https://teste/",
        "id": "9263e695-c333-4d26-b278-10e59e57df65"
    }
    requests_mock.get(f'{API_URL}v1/webhook/endpoints/9263e695-c333-4d26-b278-10e59e57df65/',
                      status_code=200, json=data)
    result = sara_sdk.retrieve(
        uuid="9263e695-c333-4d26-b278-10e59e57df65", session=default_session)
    assert result == data


def test_update(default_session, requests_mock):
    data = {
        "url": "https://teste/"
    }
    requests_mock.patch(f'{API_URL}v1/webhook/endpoints/9263e695-c333-4d26-b278-10e59e57df65/',
                        status_code=200, json=data)
    result = sara_sdk.update(
        uuid="9263e695-c333-4d26-b278-10e59e57df65", url=data, session=default_session)
    assert result == data


def test_delete(default_session, requests_mock):
    requests_mock.delete(f'{API_URL}v1/webhook/endpoints/9263e695-c333-4d26-b278-10e59e57df65/',
                         status_code=204, json={'detail': 'Endpoint deleted successfully'})
    result = sara_sdk.delete(
        uuid="9263e695-c333-4d26-b278-10e59e57df65", session=default_session)
    assert result['detail'] == 'Endpoint deleted successfully'


def test_list_relations(default_session, requests_mock):
    data = {
        "count": 1,
        "limit": 10,
        "results": [
            {
                "createdAt": "2021-07-12T12:57:27.036Z",
                "id": "f710a58f-2ed0-4379-b057-0eb633254cf4",
                "topic": "telemetry/RetrieveRobotPose",
                "endpoint": "b53a6184-df01-4718-903e-52c946507ac5",
                "robot": "f8b85a7a-4540-4d46-a2ed-00e6134ee84a"
            }
        ]
    }
    requests_mock.get(f'{API_URL}v1/webhook/endpoints/9263e695-c333-4d26-b278-10e59e57df65/relations/',
                      status_code=200, json=data)
    result = sara_sdk.list_relations(
        endpoint="9263e695-c333-4d26-b278-10e59e57df65", session=default_session)
    assert result == data


def test_create_relations(default_session, requests_mock):
    data = {
        "robots": ["f8b85a7a-4540-4d46-a2ed-00e6134ee84a"],
        "topics": ["telemetry/RetrieveRobotPose"]
    }
    requests_mock.post(f'{API_URL}v1/webhook/endpoints/9263e695-c333-4d26-b278-10e59e57df65/relations/',
                       status_code=202, text="Accepted")
    result = sara_sdk.create_relations(
        endpoint="9263e695-c333-4d26-b278-10e59e57df65", robot=data["robots"], topic=data["topics"], session=default_session)
    assert result == "Accepted"


def test_delete_relations(default_session, requests_mock):
    requests_mock.delete(f'{API_URL}v1/webhook/endpoints/9263e695-c333-4d26-b278-10e59e57df65/relations/relation_uuid/',
                         status_code=204, json={'detail': 'Relation deleted successfully'})
    result = sara_sdk.delete_relations(
        endpoint="9263e695-c333-4d26-b278-10e59e57df65", uuid="relation_uuid", session=default_session)
    assert result['detail'] == 'Relation deleted successfully'
