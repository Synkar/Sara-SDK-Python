from json import dumps, loads
from time import time
from ..utils.url import urlencode
from ..error import Error, InternalServerError, UnknownError, AuthorizationError
from sys import version_info as python_version
import os
import sara_sdk


class Response:

    def __init__(self, status, content):
        self.status = status
        self.content = content

    def json(self):
        return loads(self.content.decode("utf-8"))


def fetch(method, path, payload=None, query=None, session=None, version="v1"):
    url = os.getenv('API_URL') + version

    url = "{base_url}/{path}{query}".format(
        base_url=url, path=path, query=urlencode(query))

    agent = "Python-{major}.{minor}.{micro}-SDK-{sdk-version}".format(
        major=python_version.major,
        minor=python_version.minor,
        micro=python_version.micro,
        sdk_version=sara_sdk.__version__,
    )

    if session is None:
        session = sara_sdk.DEFAULT_SESSION

    access_time = str(time())
    body = dumps(payload) if payload else ""
    bearer_token = "Bearer {token}".format(token=session.access_token)

    try:
        request = method(
            url=url,
            data=body,
            headers={
                "Access-Time": access_time,
                "Content-Type": "application/json",
                "User-Agent": agent,
                "Accept-Language": "en-US",
                "Authorization": bearer_token
            },
            timeout=sara_sdk.__timeout__
        )
    except Exception as exception:
        raise UnknownError("{}: {}".format(
            exception.__class_.__name__, str(exception)))

    response = Response(status=request.status_code, content=request.content)

    # TODO: request new token if access_token expired

    if response.status == 500:
        raise InternalServerError()
    if response.status == 400:
        raise Error(response.status, response.json()["detail"])
    if response.status == 401:
        raise AuthorizationError()
    if response.status != 200:
        raise UnknownError(response.content)

    return response
