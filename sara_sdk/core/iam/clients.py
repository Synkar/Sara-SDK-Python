from sara_sdk.common.session import Session
from ...utils.rest import retrieve as _retrieve, list as _list, update as _update, delete as _delete, create as _create

RESOURCE = "iam/clients"


def list(session: Session = None, **filters):
    """
    List a array of clients

    Args:
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of clients

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> list(page=1,page_size=10,name="client name")
    """
    result = _list(resource=RESOURCE, session=session, **filters)
    return result
