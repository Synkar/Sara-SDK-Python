from typing import Dict
from ...client.requests import fetch
from sara_sdk.common.session import Session
from ...utils.rest import list as _list, list_paginated as _list_paginated, create as _create
import json

RESOURCE = "srs/activities"


def list(session: Session = None, **filters):
    """
    List activities

    Args:
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of activities

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> list(page=1,page_size=10,name="bucket name")
    """
    result = _list(resource=RESOURCE, session=session, **filters)
    return result


def list_paginated(session: Session = None, **filters):
    """
    List iterator of activities pages

    Args:
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of activities

    Returns:
      result (json): returns the result of the request as json by page

    Example:
      >>> next(list(page=1,page_size=10,name="bucket name"))
    """
    result = _list_paginated(resource=RESOURCE, session=session,
                             version="v2", **filters)
    return result


def create(relationship: str, type: Dict, robots: list, files: list, session: Session = None, **data):
    """
    Create an activity

    Args:
      relationship (str): relationship uuid
      type (str): operation to create an activity (D: 'DownloadFile', U: 'UploadFile')
      robots (list[str]): list of robots uuid
      files (list[str]): list of files uuid
      session (Session): Used only if want to use a different session instead default
      data (Any): data to create a activity

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> create(relationship="uuid",type="D",robots=["uuid"],files=["uuid"],data={"name":"activity name"})
    """

    payload = {
        "type": type,
        "robots": json.dumps(robots),
        "files": json.dumps(files)
    }

    result = _create("srs/relationships/{}/activities".format(
                     relationship), payload=payload, session=session)
    return result
