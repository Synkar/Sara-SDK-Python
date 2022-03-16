from requests import get, post, delete as _delete, patch
from ..client.requests import fetch


def retrieve(resource, id, session=None, **kwargs):
    path = "{endpoint}/{id}/".format(endpoint=resource, id=id)
    json = fetch(method=get, path=path, query=kwargs, user=session).json()
    return json


def list(resource, session=None, **kwargs):
    json = fetch(method=get, path=resource, query=kwargs, user=session).json()
    return json


def create(resource, payload, session=None, **kwargs):
    json = fetch(method=post, path=resource, user=session,
                 query=kwargs, payload=payload).json()
    return json


def delete(resource, id, session=None):
    path = "{endpoint}/{id}/".format(endpoint=resource, id=id)
    json = fetch(method=_delete, path=path, user=session).json()
    return json


def update(resource, id, session=None, **payload):
    path = "{endpoint}/{id}/".format(endpoint=resource, id=id)
    json = fetch(method=patch, path=path, user=session, payload=payload).json()
    return json
