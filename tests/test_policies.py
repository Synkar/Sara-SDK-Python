from sara_sdk.common.session import Session
from dotenv import load_dotenv
from sara_sdk import API_URL
import pytest
import os
import sara_sdk.core.iam.policies as sara_sdk


@pytest.fixture
def default_session():

    load_dotenv()
    ACCESS_KEY = os.getenv('ACCESS_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    new_session = Session(ACCESS_KEY, SECRET_KEY)
    new_session.auth()
    return new_session


def test_policies_create(default_session, requests_mock):
    model = {
        "name": "test policy",
        "description": "description test",
        "scope": 0,
        "resource": 0,
        "client": "f89356bd-294d-4f55-8395-c4825a296b95"
    }
    requests_mock.post(f'{API_URL}v1/iam/policies/',
                       status_code=202, json=model)
    result = sara_sdk.create(model=model, session=default_session)
    assert result == model


def test_policies_list(default_session, requests_mock):
    data = [{'name': 'test policy'}]
    requests_mock.get(f'{API_URL}v1/iam/policies/?page=1&page_size=10',
                      status_code=202, json=data)
    result = sara_sdk.list(session=default_session, page=1, page_size=10)
    assert result == data


def test_policies_retrieve(default_session, requests_mock):
    requests_mock.get(f'{API_URL}v1/iam/policies/00ea03f1-5b2e-4787-8aa6-745961c6d506/',
                      status_code=202, json={'uuid': '00ea03f1-5b2e-4787-8aa6-745961c6d506'})
    result = sara_sdk.retrieve(
        uuid='00ea03f1-5b2e-4787-8aa6-745961c6d506', session=default_session)
    assert result["uuid"] == '00ea03f1-5b2e-4787-8aa6-745961c6d506'


def test_policies_delete(default_session, requests_mock):
    requests_mock.delete(f'{API_URL}v1/iam/policies/00ea03f1-5b2e-4787-8aa6-745961c6d506/',
                         status_code=202, json={'detail': 'Policy deleted successfully'})
    result = sara_sdk.delete(
        uuid='00ea03f1-5b2e-4787-8aa6-745961c6d506', session=default_session)
    assert result["detail"] == 'Policy deleted successfully'


def test_policies_update(default_session, requests_mock):
    model = {
        'name': 'New name policy'
    }
    requests_mock.patch(f'{API_URL}v1/iam/policies/00ea03f1-5b2e-4787-8aa6-745961c6d506/',
                        status_code=202, json={'uuid': '00ea03f1-5b2e-4787-8aa6-745961c6d506', 'name': 'New name policy'})
    result = sara_sdk.update(
        uuid='00ea03f1-5b2e-4787-8aa6-745961c6d506', model=model, session=default_session)
    assert result['uuid'] == '00ea03f1-5b2e-4787-8aa6-745961c6d506'


def test_policies_attach_action(default_session, requests_mock):
    requests_mock.post(f'{API_URL}v1/iam/policies/cba10317-cfb0-465e-9f7f-8a3a51bf8cac/attachPermissions/',
                       status_code=200, json={'detail': 'Action attached successfully'})
    result = sara_sdk.attachAction("2d1cb23c-181c-4c28-b078-9574ea84ff18",
                                   "cba10317-cfb0-465e-9f7f-8a3a51bf8cac", default_session)

    assert result["detail"] == "Action attached successfully"


def test_policies_detach_action(default_session, requests_mock):
    requests_mock.delete(f'{API_URL}v1/iam/policies/cba10317-cfb0-465e-9f7f-8a3a51bf8cac/attachAction/',
                         status_code=200, json={'detail': 'Action detached successfully'})
    result = sara_sdk.detachAction("2d1cb23c-181c-4c28-b078-9574ea84ff18",
                                   "cba10317-cfb0-465e-9f7f-8a3a51bf8cac", default_session)

    assert result["detail"] == "Action detached successfully"
