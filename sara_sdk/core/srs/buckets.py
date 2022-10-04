from io import BufferedReader
from typing import Dict

from requests import get, post
from ...client.requests import fetch

from sara_sdk.common.session import Session
from ...utils.rest import retrieve as _retrieve, list as _list, list_paginated as _list_paginated, update as _update, delete as _delete, create as _create

RESOURCE = "srs/buckets"


def list(session: Session = None, **filters):
    """
    List buckets

    Args:
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of buckets

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> list(page=1,page_size=10,name="bucket name")
    """
    result = _list(resource=RESOURCE, session=session, **filters)
    return result


def list_paginated(session: Session = None, **filters):
    """
    List iterator of buckets pages

    Args:
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of buckets

    Returns:
      result (json): returns the result of the request as json by page

    Example:
      >>> next(list(page=1,page_size=10,name="bucket name"))
    """
    result = _list_paginated(resource=RESOURCE, session=session,
                             version="v2", **filters)
    return result

def retrieve(uuid: str, session: Session = None):
    """
    Retrieve a bucket by uuid

    Args:
      uuid (UUID): uuid to return a bucket
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> retrieve("230dd69a-0470-4542-93ef-8fb75ff4e3be")
    """
    result = _retrieve(RESOURCE, uuid, session=session)
    return result

def create(model: Dict, session: Session = None):
    """
    Create a bucket

    Args:
      model (Dict): model of the bucket
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> create({ "name": "bucket-test-public", "locality": "sp_ribeirao_sy", "type": "PUBLIC", "all_clients_permitted": "true" })
    """
    result = _create(RESOURCE, payload=model, session=session)
    return result

def update(uuid: str, model: Dict, session: Session = None):
    """
    Update a bucket

    Args:
      uuid (UUID): uuid of the bucket to be updated
      model (Dict): model of the bucket to be updated
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> update("f8b85a7a-4540-4d46-a2ed-00e6134ee84a", { "name": "bucket-test-private-changed"})
    """
    result = _update(RESOURCE, uuid, payload=model, session=session)
    return result

def delete(uuid: str, session: Session = None):
    """
    Delete a bucket

    Args:
      uuid (UUID): uuid of the bucket
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> delete("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = _delete(RESOURCE, uuid, session=session)
    return result

def upload(uuid: str, path: str, file: BufferedReader, session: Session = None):
    """
    Upload a file to a bucket

    Args:
      uuid (UUID): uuid of the bucket
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> upload("f8b85a7a-4540-4d46-a2ed-00e6134ee84a", path="folder" file=open("test-file.txt", "rb"))
    """
    model = {
        "key": "{}/{}".format(path, file.name)
    }
    outromodel = {
        "file": file
    }
    result = fetch(
        path="{}/{}/upload".format(RESOURCE, uuid),
        session=session,
        query=model,
        payload=outromodel,
        method=post
    )
    return result

def download(uuid: str, session: Session = None):
    """
    Download a file from a bucket

    Args:
      uuid (UUID): uuid of the bucket
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> download("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = fetch(
        RESOURCE+"/"+uuid+"/download",
        session=session,
        method=get
    )
    return result

def create_folder(uuid: str, name: str, session: Session = None):
    """
    Create a folder in a bucket

    Args:
      uuid (UUID): uuid of the bucket
      name (str): name of the folder
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> create_folder("e3ba0074-44db-4ac7-b826-d1840fc73b25", "test-folder")
    """
    model = {
      "folder": name
    }
    result = fetch(path="{}/{}/create_folder".format(RESOURCE, uuid), query=model, session=session, method=post)
    return result

def delete_object(key: str, session: Session = None):
    """
    Delete an object in a bucket

    Args:
      key (str): key of the object
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> delete_object("test.txt")
    """
    result = _delete(RESOURCE+"/"+key, session=session)
    return result
