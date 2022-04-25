from sara_sdk.common.session import Session
from dotenv import load_dotenv
from sara_sdk import API_URL
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


def test_groups_list(default_session, requests_mock):
    data = [{'name': 'groups_name'}]
    requests_mock.get(f'{API_URL}v1/iam/groups/?page=1&page_size=10',
                      status_code=200, json=data)
    result = sara_sdk.list(session=default_session, page=1, page_size=10)
    assert result == data


def test_groups_retrieve(default_session, requests_mock):
    data = {'uuid': '00ea03f1-5b2e-4787-8aa6-745961c6d506', 'name': 'groups_name'}
    requests_mock.get(f'{API_URL}v1/iam/groups/00ea03f1-5b2e-4787-8aa6-745961c6d506/',
                      status_code=200, json=data)
    result = sara_sdk.retrieve(
        uuid="00ea03f1-5b2e-4787-8aa6-745961c6d506", session=default_session)
    assert result["uuid"] == "00ea03f1-5b2e-4787-8aa6-745961c6d506"


def test_groups_update(default_session, requests_mock):
    model = {
        "name": "Teste Group"
    }
    requests_mock.patch(f'{API_URL}v1/iam/groups/00ea03f1-5b2e-4787-8aa6-745961c6d506/',
                        status_code=200, json=model)
    result = sara_sdk.update(
        uuid="00ea03f1-5b2e-4787-8aa6-745961c6d506", model=model, session=default_session)
    assert result["name"] == "Teste Group"


def test_groups_create(default_session, requests_mock):
    model = {
        "name": "Teste Group"
    }
    requests_mock.post(f'{API_URL}v1/iam/groups/',
                       status_code=200, json=model)
    result = sara_sdk.create(model=model, session=default_session)
    assert result["name"] == "Teste Group"


def test_groups_delete(default_session, requests_mock):
    requests_mock.delete(f'{API_URL}v1/iam/groups/00ea03f1-5b2e-4787-8aa6-745961c6d506/',
                         status_code=200, json={'detail': 'Group deleted successfully'})
    result = sara_sdk.delete(
        uuid="00ea03f1-5b2e-4787-8aa6-745961c6d506", session=default_session)
    assert result["detail"] == "Group deleted successfully"


def test_groups_attach_user(default_session, requests_mock):
    requests_mock.post(f'{API_URL}v1/iam/groups/cba10317-cfb0-465e-9f7f-8a3a51bf8cac/attachUserGroup/',
                       status_code=200, json={'detail': 'User attached successfully'})
    result = sara_sdk.attachUser("2d1cb23c-181c-4c28-b078-9574ea84ff18",
                                 "cba10317-cfb0-465e-9f7f-8a3a51bf8cac", default_session)

    assert result["detail"] == "User attached successfully"


def test_groups_detach_user(default_session, requests_mock):
    requests_mock.delete(f'{API_URL}v1/iam/groups/cba10317-cfb0-465e-9f7f-8a3a51bf8cac/attachUserGroup/',
                         status_code=200, json={'detail': 'User detached successfully'})
    result = sara_sdk.detachUser("2d1cb23c-181c-4c28-b078-9574ea84ff18",
                                 "cba10317-cfb0-465e-9f7f-8a3a51bf8cac", default_session)

    assert result["detail"] == "User detached successfully"


def test_groups_attach_policy(default_session, requests_mock):
    requests_mock.post(f'{API_URL}v1/iam/groups/cba10317-cfb0-465e-9f7f-8a3a51bf8cac/attachPolicy/',
                       status_code=200, json={'detail': 'Policy attached successfully'})
    result = sara_sdk.attachPolicy("2d1cb23c-181c-4c28-b078-9574ea84ff18",
                                   "cba10317-cfb0-465e-9f7f-8a3a51bf8cac", default_session)

    assert result["detail"] == "Policy attached successfully"


def test_groups_detach_policy(default_session, requests_mock):
    requests_mock.delete(f'{API_URL}v1/iam/groups/cba10317-cfb0-465e-9f7f-8a3a51bf8cac/attachPolicy/',
                         status_code=200, json={'detail': 'Policy detached successfully'})
    result = sara_sdk.detachPolicy("2d1cb23c-181c-4c28-b078-9574ea84ff18",
                                   "cba10317-cfb0-465e-9f7f-8a3a51bf8cac", default_session)

    assert result["detail"] == "Policy detached successfully"
