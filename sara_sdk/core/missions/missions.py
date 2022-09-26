from typing import Dict
import json
from sara_sdk.common.session import Session
from ...utils.rest import list as _list, list_paginated as _list_paginated, create as _create, retrieve as _retrieve
from requests import get, post, delete as _delete, patch
from ...client.requests import fetch

RESOURCE = "missions"


def list(robot: str, session: Session = None, **filters):
    """
    List a array of missions

    Args:
      robot (UUID): robot to return a mission
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of missions

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> list(page=1,page_size=10,name="mission name")
    """
    filters["robot_id"] = robot
    result = _list(resource=RESOURCE, session=session,version="v2", **filters)
    return result

def retrieve(uuid: str, session: Session = None):
    """
    Retrieve a mission by passing uuid

    Args:
      mission (UUID): mission uuid to retrieve
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> retrieve("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = _retrieve(RESOURCE, id=uuid, session=session, version="v2")
    return result


def list_paginated(robot: str, session: Session = None, **filters):
    """
    List iterator of pages of missions

    Args:
      robot (UUID): robot to return a mission
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of missions

    Returns:
      result (json): returns the result of the request as json by page

    Example:
      >>> next(list(page=1,page_size=10,name="mission name"))
    """
    filters["robot_id"] = robot
    result = _list_paginated(resource=RESOURCE, session=session,
                             version="v2", **filters)
    return result


def last(robot: str, session: Session = None):
    """
    Retrieve the last mission by robot id

    Args:
      robot (UUID): robot to return a mission
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> retrieve("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = _list(RESOURCE+"/last", session=session,
                   version="v2", robot_id=robot)
    return result


def create(robot: str, stages: Dict, session: Session = None):
    """
    Create a mission by passing an model (Data)

    Args:
      robot (UUID): robot uuid to create mission
      stages (Dict): A dictionary with the data the will be used to create an mission
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json
    """
    model = {
        "robot": robot,
        "stages": json.dumps(stages)
    }
    result = _create(RESOURCE, payload=model, session=session, version="v2")
    return result

def retry(mission: str, session: Session = None):
    """
    Retry a mission by passing uuid

    Args:
      mission (UUID): mission uuid to retry
      session (Session): Used only if want to use a different session instead default

    Returns:
      null

    Example:
      >>> retry("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = fetch(path=RESOURCE+"/"+mission+"/retry", session=session, method=post, version="v2")
    if result and result.status == 202:
        return True
    return False

def cancel(mission: str, session: Session = None):
    """
    Cancel a mission by passing uuid

    Args:
      mission (UUID): mission uuid to cancel
      session (Session): Used only if want to use a different session instead default

    Returns:
      null

    Example:
      >>> cancel("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = fetch(path=RESOURCE+"/"+mission+"/cancel", session=session, method=post, version="v2")
    if result and result.status == 202:
        return True
    return False

def pause(mission: str, session: Session = None):
    """
    Pause a mission by passing uuid

    Args:
      mission (UUID): mission uuid to pause
      session (Session): Used only if want to use a different session instead default

    Returns:
      null

    Example:
      >>> pause("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = fetch(path=RESOURCE+"/"+mission+"/pause", session=session, method=post, version="v2")
    if result and result.status == 202:
        return True
    return False

def resume(mission: str, session: Session = None):
    """
    Resume a mission by passing uuid

    Args:
      mission (UUID): mission uuid to resume
      session (Session): Used only if want to use a different session instead default

    Returns:
      null

    Example:
      >>> resume("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = fetch(path=RESOURCE+"/"+mission+"/resume", session=session, method=post, version="v2")
    if result and result.status == 202:
        return True
    return False