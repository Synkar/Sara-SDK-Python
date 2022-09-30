from typing import Dict
import json
from sara_sdk.common.session import Session
from ...utils.rest import retrieve as _retrieve, list as _list, update as _update, delete as _delete, create as _create


RESOURCE = "webhooks/endpoints"


def list(session: Session = None, **filters):
    """
    List a array of endpoints

    Args:
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of endpoints

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> list(page=1,page_size=10,name="endpoint name")
    """
    result = _list(resource=RESOURCE, session=session, **filters)
    return result


def create(url: str, session: Session = None):
    """
    Create a new endpoint

    Args:
      name (string): name of the endpoint
      url (string): url of the endpoint
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of request as json

    Example:
      >>> create("https://endpoint.url")
    """
    data = {"url": url}
    result = _create(resource=RESOURCE, data=data, session=session)
    return result


def retrieve(uuid: str, session: Session = None):
    """
    Retrieve a endpoint

    Args:
      uuid (string): uuid of the endpoint
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of request as json

    Example:
      >>> retrieve("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = _retrieve(resource=RESOURCE, uuid=uuid, session=session)
    return result


def update(uuid: str, url: str, session: Session = None):
    """
    Update a endpoint

    Args:
      uuid (string): uuid of the endpoint
      url (string): url of the endpoint
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of request as json

    Example:
      >>> update("f8b85a7a-4540-4d46-a2ed-00e6134ee84a", "https://endpoint.url")
    """
    data = {"url": url}
    result = _update(resource=RESOURCE, uuid=uuid, data=data, session=session)
    return result


def delete(uuid: str, session: Session = None):
    """
    Delete a endpoint

    Args:
      uuid (string): uuid of the endpoint
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of request as json

    Example:
      >>> delete("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = _delete(resource=RESOURCE, uuid=uuid, session=session)
    return result
