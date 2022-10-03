from typing import Dict
from sara_sdk.common.session import Session
from ...utils.rest import retrieve as _retrieve, list as _list, update as _update, delete as _delete, create as _create
from ...client.requests import fetch

RESOURCE = "webhook/event-executions"


def list(endpoint: str, session: Session = None, **filters):
    """
    List a array of event executions

    Args:
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of event executions

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> list(page=1,page_size=10, endpoint="endpoint_uuid")
    """
    filters["endpoint"] = endpoint
    result = _list(resource=RESOURCE, session=session, **filters)
    return result
