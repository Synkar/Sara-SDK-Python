from sara_sdk.common.session import Session
from dotenv import load_dotenv
from sara_sdk import API_URL
import pytest
import os
import sara_sdk.core.missions.tags as sara_sdk

@pytest.fixture
def default_session():

    load_dotenv()
    ACCESS_KEY = os.getenv('ACCESS_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    new_session = Session(ACCESS_KEY, SECRET_KEY)
    new_session.auth()
    return new_session

def test_tags_list(default_session, requests_mock):
    data = [{
        'uuid': 'tag_uuid',
        'name': 'tag_name',
    }]
    requests_mock.get(f'{API_URL}v2/missions/tags/?page=1&page_size=10',
                      status_code=200, json=data)
    result = sara_sdk.list(session=default_session, page=1, page_size=10)
    assert result == data

def test_tags_retrieve(default_session, requests_mock):
    data = {
        'uuid': 'tag_uuid',
        'name': 'tag_name',
    }
    requests_mock.get(f'{API_URL}v2/missions/tags/tag_uuid/',
                      status_code=200, json=data)
    result = sara_sdk.retrieve(
        uuid="tag_uuid", session=default_session)
    assert result["uuid"] == "tag_uuid"

def test_tags_list_paginated(default_session, requests_mock):
    data_page1 = {
        'next': 2,
        'count': 2,
        'previous': None,
        'results': [{
            "uuid": "53dc35e0-df90-44fb-abee-c3f3c62b3a77",
            "name": "teste",
            "group": "",
            "datetime_created": "2022-04-09T01:28:40.634092Z",
            "datetime_used": "2022-09-19T22:12:05.750247Z"},
        ]
    }
    data_page2 = {
        'next': None,
        'count': 2,
        'previous': 1,
        'results': [
            {
            "uuid": "e0870e22-b407-4539-a694-79ea866eba9a",
            "name": "autonomous mode",
            "group": "",
            "datetime_created": "2022-08-09T21:17:01.812059Z",
            "datetime_used": "2022-08-09T21:17:01.812083Z"
        }]
    }
    requests_mock.get(f'{API_URL}v2/missions/tags/?page=1&page_size=1',
                      status_code=200, json=data_page1)
    requests_mock.get(f'{API_URL}v2/missions/tags/?page=2&page_size=1',
                      status_code=200, json=data_page2)
    result = sara_sdk.list_paginated(session=default_session, page_size=1)
    assert list(result) == [data_page1['results'], data_page2['results']]

def test_tags_create(default_session, requests_mock):
    data = {
        'name': 'tag_name',
    }
    requests_mock.post(f'{API_URL}v2/missions/tags/',
                       status_code=200, json=data)
    result = sara_sdk.create(model=data, session=default_session)
    assert result == data

def test_tags_delete(default_session, requests_mock):
    requests_mock.delete(f'{API_URL}v2/missions/tags/tag_uuid/',
                         status_code=200, json={'detail': 'Tag deleted successfully'})
    result = sara_sdk.delete(uuid="tag_uuid", session=default_session)
    assert result['detail'] == 'Tag deleted successfully'