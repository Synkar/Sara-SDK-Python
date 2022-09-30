from typing import Dict
import json
from sara_sdk.common.session import Session
from ...utils.rest import retrieve as _retrieve, list as _list, update as _update, delete as _delete, create as _create

RESOURCE = "webhooks/topics"


def list(session: Session = None, **filters):
    """
    List a array of topics

    Args:
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of topics

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> list(page=1,page_size=10,name="topic name")
    """
    result = _list(resource=RESOURCE, session=session, **filters)
    return result


def create(name: str, session: Session = None):
    """
    Create a new topic

    Args:
      name (string): name of the topic
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of request as json

    Example:
      >>> create("topic.name")
    """
    data = {"name": name}
    result = _create(resource=RESOURCE, data=data, session=session)
    return result


def delete(uuid: str, session: Session = None):
    """
    Delete a topic

    Args:
      uuid (string): uuid of the topic
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of request as json

    Example:
      >>> delete("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = _delete(resource=RESOURCE, uuid=uuid, session=session)
    return result
