from requests import get, post, delete as _delete, patch
from ..client.requests import fetch


def retrieve(resource, id, session=None, **kwargs):
    """
    Retrieve function to request a GET passing id to the API

    Args:
        resource (string): the route to access on the api
        id (string): uuid to the resource
        session (Session): session where to get the authorization (only needed if doens't want
        to use the DEFAULT_SESSION)
        kwargs (any): will be used as query to the route

    Returns:
        Json: The json of the content of the response sended by the api

    Example:
        >>> retrieve(resource="iam/robots", "09594aae-7e88-4c8b-b4e5-095c6e785509")
    """
    path = "{endpoint}/{id}/".format(endpoint=resource, id=id)
    json = fetch(method=get, path=path, query=kwargs, session=session).json()
    return json


def list(resource, session=None, **kwargs):
    """
    List function to request a GET to receive a list of objects

    Args:
        resource (string): the route to access on the api
        session (Session): session where to get the authorization (only needed if doens't want
        to use the DEFAULT_SESSION)
        kwargs (any): will be used as query to the route

    Returns:
        Json: The json of the content of the response sended by the api

    Example:
        >>> list(resource="iam/robots")
    """
    json = fetch(method=get, path=resource,
                 query=kwargs, session=session).json()
    return json


def create(resource, payload, session=None, **kwargs):
    """
    Create function to request a POST to create a new instance of resource

    Args:
        resource (string): the route to access on the api
        payload (Dict): A dict with data to use to create the new resource
        session (Session): session where to get the authorization (only needed if doens't want
        to use the DEFAULT_SESSION)
        kwargs (any): will be used as query to the route

    Returns:
        Json: The json of the content of the response sended by the api

    Example:
        >>> create(resource="iam/robots", payload=Dict)
    """
    json = fetch(method=post, path=resource, session=session,
                 query=kwargs, payload=payload).json()
    return json


def delete(resource, id, session=None):
    """
    Delete function to request a DELETE passing id to the API

    Args:
        resource (string): the route to access on the api
        id (string): uuid to the resource
        session (Session): session where to get the authorization (only needed if doens't want
        to use the DEFAULT_SESSION)
        kwargs (any): will be used as query to the route

    Returns:
        Json: The json of the content of the response sended by the api

    Example:
        >>> delete(resource="iam/robots", "09594aae-7e88-4c8b-b4e5-095c6e785509")
    """
    path = "{endpoint}/{id}/".format(endpoint=resource, id=id)
    json = fetch(method=_delete, path=path, session=session).json()
    return json


def update(resource, id, session=None, **payload):
    """
    Delete function to request a DELETE passing id to the API

    Args:
        resource (string): the route to access on the api
        id (string): uuid to the resource
        session (Session): session where to get the authorization (only needed if doens't want
        to use the DEFAULT_SESSION)
        payload (Dict): A dict with data to use to update the resource

    Returns:
        Json: The json of the content of the response sended by the api

    Example:
        >>> delete(resource="iam/robots", "09594aae-7e88-4c8b-b4e5-095c6e785509", payload=Dict)
    """
    path = "{endpoint}/{id}/".format(endpoint=resource, id=id)
    json = fetch(method=patch, path=path,
                 session=session, payload=payload).json()
    return json
