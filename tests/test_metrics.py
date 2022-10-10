from sara_sdk.common.session import Session
from dotenv import load_dotenv
from sara_sdk import API_URL
import pytest
import os
import sara_sdk.core.metrics.metrics as sara_sdk


@pytest.fixture
def default_session():

    load_dotenv()
    ACCESS_KEY = os.getenv('ACCESS_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    new_session = Session(ACCESS_KEY, SECRET_KEY)
    new_session.auth()
    return new_session


def test_metrics_retrieve(default_session, requests_mock):
    data = [{
        "_measurement": "missions_v2_status",
        "assisted": "False",
        "outcome": "0",
        "robot": "144cdc28-9126-4f59-b32b-307b2ae43fb3",
        "stage": "f51fd3e3-9970-4373-b016-1e69482744a2",
        "status": "10"
    }]
    requests_mock.post(
        f'{API_URL}v1/metrics/missions_v2_status/', status_code=200, json=data)
    result = sara_sdk.retrieve(
        measurement="missions_v2_status", range="start:-5m", session=default_session)
    assert result == data
