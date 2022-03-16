from base64 import b64encode, standard_b64encode
from requests import post
from time import time
from sys import version_info as python_version
from ..error import InternalServerError, InputErrors, UnknownError
from ..client.requests import Response
import os
import sara_sdk


class Session:
    """
    Session model responsable to maintain data access, you can use the DEFAULT_SESSION by just
    using the sara_sdk.auth() but can create other sessions using this class and passing on
    others functions by the param session

    Args:
        access_key (string): Access Key used to authenticate the user on Sara API
        secret_access_key (string): Secret Key used to authenticate the user on Sara API
    """

    def __init__(self, access_key, secret_access_key):
        self.access_key = access_key
        self.secret_access_key = secret_access_key
        self.access_token = ""

    def auth(self):
        """
        Authenticate the session using the oauth2.0 on aws cognito

        Returns:
            Response: A object of Response with status and content data

        Examples:
            >>> result = Session.auth();
        """
        url = sara_sdk.AUTH_URL
        body = {

        }
        access_time = str(time())

        agent = "Python-{major}.{minor}.{micro}-Sara-SDK-{sdk_version}".format(
            major=python_version.major,
            minor=python_version.minor,
            micro=python_version.micro,
            sdk_version=sara_sdk.__version__,
        )

        auth = "{access}:{secret}".format(
            access=self.access_key, secret=self.secret_access_key)

        try:
            request = post(url=url,
                           data=body,
                           headers={
                               "Access-Time": access_time,
                               "Content-Type": "application/json",
                               "User-Agent": agent,
                               "Accept-Language": "en-US",
                               "Authorization": standard_b64encode(auth)
                           },
                           timeout=sara_sdk.__timeout__)
        except Exception as exception:
            raise UnknownError("{}: {}".format(
                exception.__class_.__name__, str(exception)))

        response = Response(status=request.status_code,
                            content=request.content)

        if response.content is not None:
            payload = response.json()
            self.access_token = payload.access_token
            self.expires_in = payload.expires_in
            self.token_type = payload.token_type

        if response.status == 500:
            raise InternalServerError()
        if response.status == 400:
            raise InputErrors(response.json()["errors"])
        if response.status != 200:
            raise UnknownError(response.content)

        return response
