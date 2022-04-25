from sara_sdk.common.session import Session
from dotenv import load_dotenv
from sara_sdk import API_URL
import pytest
import os
import sara_sdk.core.iam.fleets as sara_sdk


@pytest.fixture
def default_session():

    load_dotenv()
    ACCESS_KEY = os.getenv('ACCESS_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    new_session = Session(ACCESS_KEY, SECRET_KEY)
    new_session.auth()
    return new_session


def test_fleets_list(default_session, requests_mock):
    data = [{'name': 'fleet_name'}]
    requests_mock.get(f'{API_URL}v1/iam/fleets/?page=1&page_size=10',
                      status_code=200, json=[{'name': 'fleet_name'}])
    result = sara_sdk.list(session=default_session, page=1, page_size=10)
    assert result == data


def test_fleets_retrieve(default_session, requests_mock):
    requests_mock.get(f'{API_URL}v1/iam/fleets/3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc/',
                      status_code=200, json={'uuid': '3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc', 'name': 'fleet_name'})
    result = sara_sdk.retrieve(
        uuid="3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc", session=default_session)
    assert result["uuid"] == "3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc"


def test_fleets_update(default_session, requests_mock):
    model = {
        "name": "Test Fleet"
    }
    requests_mock.patch(f'{API_URL}v1/iam/fleets/3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc/',
                        status_code=200, json={'uuid': '3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc', 'name': 'Test Fleet'})
    result = sara_sdk.update(
        uuid="3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc", model=model, session=default_session)
    assert result["name"] == "Test Fleet"


def test_fleets_create(default_session, requests_mock):
    model = {
        "name": "Test Fleet"
    }
    requests_mock.post(f'{API_URL}v1/iam/fleets/',
                       status_code=201, json={'uuid': '3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc', 'name': 'Test Fleet'})
    result = sara_sdk.create(model, default_session)
    assert result["name"] == "Test Fleet"


def test_fleets_delete(default_session, requests_mock):
    requests_mock.delete(f'{API_URL}v1/iam/fleets/3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc/',
                         status_code=200, json={'detail': 'Fleet deleted successfully'})
    result = sara_sdk.delete(
        uuid="3ddc1eb5-8433-4eca-a95d-ff2d688cc2fc", session=default_session)
    assert result["detail"] == "Fleet deleted successfully"


def test_fleets_attach_robot(default_session, requests_mock):
    requests_mock.post(f'{API_URL}v1/iam/fleets/cba10317-cfb0-465e-9f7f-8a3a51bf8cac/attachRobot/',
                       status_code=200, json={'detail': 'Robot attached successfully'})
    result = sara_sdk.attachRobot("2d1cb23c-181c-4c28-b078-9574ea84ff18",
                                  "cba10317-cfb0-465e-9f7f-8a3a51bf8cac", default_session)

    assert result["detail"] == "Robot attached successfully"


def test_fleets_detach_robot(default_session, requests_mock):
    requests_mock.delete(f'{API_URL}v1/iam/fleets/cba10317-cfb0-465e-9f7f-8a3a51bf8cac/attachRobot/',
                         status_code=200, json={'detail': 'Robot detached successfully'})
    result = sara_sdk.detachRobot("2d1cb23c-181c-4c28-b078-9574ea84ff18",
                                  "cba10317-cfb0-465e-9f7f-8a3a51bf8cac", default_session)

    assert result["detail"] == "Robot detached successfully"
