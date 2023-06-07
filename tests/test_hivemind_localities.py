import json
from unittest import result
from sara_sdk.common.session import Session
from dotenv import load_dotenv
from sara_sdk import API_URL
import pytest
import os
import sara_sdk.core.hivemind.localities as sara_sdk


@pytest.fixture
def default_session():
  load_dotenv()
  ACCESS_KEY = os.getenv('ACCESS_KEY')
  SECRET_KEY = os.getenv('SECRET_KEY')
  new_session = Session(ACCESS_KEY, SECRET_KEY)
  new_session.auth()
  return new_session

def test_localities_list(default_session, requests_mock):
  data = {
      'next': None,
      'count': 1,
      'previous': None,
      'results': [{
          "slug": "test_locality",
      }]
  }
  requests_mock.get(f'{API_URL}v1/hivemind/localities/?page=1&page_size=10',
                    status_code=200, json=data)
  result = sara_sdk.list(session=default_session, page=1, page_size=10)
  assert result == data

def test_localities_retrieve(default_session, requests_mock):
  data = {
      'slug': 'test_locality',
  }
  requests_mock.get(f'{API_URL}v1/hivemind/localities/test_locality/',
                    status_code=200, json=data)
  result = sara_sdk.retrieve(
      uuid="test_locality", session=default_session)
  assert result["slug"] == "test_locality"

def test_localities_list_paginated(default_session, requests_mock):
  data_page1 = {
      'next': 2,
      'count': 1,
      'previous': None,
      'results': [{
          "slug": "test_locality",
      }]
  }
  data_page2 = {
      'next': None,
      'count': 1,
      'previous': 1,
      'results': [{
          "slug": "test_locality",
      }]
  }
  requests_mock.get(f'{API_URL}v1/hivemind/localities/?page=1&page_size=1',
                    status_code=200, json=data_page1)
  requests_mock.get(f'{API_URL}v1/hivemind/localities/?page=2&page_size=1',
                    status_code=200, json=data_page2)
  result = sara_sdk.list_paginated(session=default_session, page_size=1)
  assert list(result) == [data_page1['results'], data_page2['results']]
  
def test_localities_update(default_session, requests_mock):
  data = {
      'slug': 'test_locality',
  }
  requests_mock.patch(f'{API_URL}v1/hivemind/localities/test_locality/',
                      status_code=200, json=data)
  result = sara_sdk.update(
      uuid="test_locality", model=data, session=default_session)
  assert result["slug"] == "test_locality"

def test_localities_create(default_session, requests_mock):
  data = {
      'slug': 'test_locality',
  }
  requests_mock.post(f'{API_URL}v1/hivemind/localities/',
                      status_code=200, json=data)
  result = sara_sdk.create(
      model=data, session=default_session)
  assert result["slug"] == "test_locality"

def test_localities_delete(default_session, requests_mock): 
  requests_mock.delete(f'{API_URL}v1/hivemind/localities/test_locality/',
                      status_code=200, json={})
  result = sara_sdk.delete(
      uuid="test_locality", session=default_session)
  assert result == {}