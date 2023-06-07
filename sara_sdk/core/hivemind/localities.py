from typing import Dict

from sara_sdk.common.session import Session
from ...utils.rest import retrieve as _retrieve, list as _list, list_paginated as _list_paginated, update as _update, delete as _delete, create as _create

RESOURCE = "hivemind/localities"

def list(session: Session = None, **filters):
  """
    List a array of localities

    Args:
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of localities

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> list(page=1,page_size=10,slug="locality slug")
  """
  result = _list(resource=RESOURCE, session=session, **filters)
  return result

def list_paginated(session: Session = None, **filters):
  """
    List a array of localities paginated

    Args:
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of localities

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> list(page=1,page_size=10,slug="locality slug")
  """
  result = _list_paginated(resource=RESOURCE, session=session, **filters)
  return result

def retrieve(uuid: str, session: Session = None):
  """
    Retrieve a locality by uuid

    Args:
      uuid (string): locality uuid to retrieve
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json
      
    Example:
      >>> retrieve("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
  """
  result = _retrieve(RESOURCE, id=uuid, session=session)
  return result

def update(uuid: str, model: Dict, session: Session = None):
  """
    Update a locality by passing uuid and an model (Data to update)

    Args:
      uuid (string): locality uuid to retrieve
      model (Dict): A dictionary with the data the will be updated on locality
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json
      
    Example:
      >>> update("f8b85a7a-4540-4d46-a2ed-00e6134ee84a", { "robotCapacity": "2" })
  """
  result = _update(RESOURCE, id=uuid, payload=model, session=session)
  return result

def delete(uuid: str, session: Session = None):
  """
    Delete a locality by uuid

    Args:
      uuid (string): locality uuid to retrieve
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> delete("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
  """
  result = _delete(RESOURCE, id=uuid, session=session)
  return result

def create(model: Dict, session: Session = None):
  """
    Create a locality by passing a model (Data to create)

    Args:
      model (Dict): A dictionary with the data the will be created on locality
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> create({ "name": "locality name" })
  """
  result = _create(RESOURCE, payload=model, session=session)
  return result