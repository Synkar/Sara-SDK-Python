from typing import Dict

from sara_sdk.common.session import Session
from ...utils.rest import retrieve as _retrieve, list as _list, list_paginated as _list_paginated, update as _update, delete as _delete, create as _create

RESOURCE = "hivemind/requests"

def list(session: Session = None, **filters):
  """
    List a array of requests

    Args:
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of requests

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> list(page=1,page_size=10,name="request name")
  """
  result = _list(resource=RESOURCE, session=session, **filters)
  return result

def list_paginated(session: Session = None, **filters):
  """
    List a array of requests paginated

    Args:
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of requests

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> list(page=1,page_size=10,name="request name")
  """
  result = _list_paginated(resource=RESOURCE, session=session, **filters)
  return result

def retrieve(uuid: str, session: Session = None):
  """
    Retrieve a request by uuid

    Args:
      uuid (string): request uuid to retrieve
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> retrieve("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
  """
  result = _retrieve(RESOURCE, id=uuid, session=session)
  return result

def create(model: Dict, session: Session = None):
  """
    Create a request by passing a model (Data to create)

    Args:
      model (Dict): A dictionary with the data the will be used to create a request
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> create({ "name": "new name" })
  """
  result = _create(RESOURCE, payload=model, session=session)
  return result
