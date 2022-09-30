from typing import Dict
import json
from sara_sdk.common.session import Session
from ...utils.rest import retrieve as _retrieve, list as _list, update as _update, delete as _delete, create as _create

RESOURCE = "webhooks/relations"


def list(session: Session = None, **filters):
    """
    List a array of relations

    Args:
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of relations

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> list(page=1,page_size=10,name="relation name")
    """
    result = _list(resource=RESOURCE, session=session, **filters)
    return result


def create(endpoint: str, event: str, session: Session = None):
    """
    Create a new relation

    Args:
      endpoint (string): uuid of the endpoint
      event (string): name of the event
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of request as json

    Example:
      >>> create("f8b85a7a-4540-4d46-a2ed-00e6134ee84a", "event.name")
    """
    data = {"endpoint": endpoint, "event": event}
    result = _create(resource=RESOURCE, data=data, session=session)
    return result


def delete(uuid: str, session: Session = None):
    """
    Delete a relation

    Args:
      uuid (string): uuid of the relation
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of request as json

    Example:
      >>> delete("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = _delete(resource=RESOURCE, uuid=uuid, session=session)
    return result
