from dotenv import load_dotenv
from .common.session import Session

__version__ = "0.0.1"
__timeout__ = 15

load_dotenv()


DEFAULT_SESSION = None
AUTH_URL = "https://auth.sara.synkar.com/oauth2/token"


def setup_default_session(access_key, secret_access_key):
    """
    Set up a default session, using the access_key and secret_key and call auth to authenticate

    Args:
      access (string): Access Key used to authenticate the user on Sara API
      secret (string): Secret Key used to authenticate the user on Sara API

    """
    global DEFAULT_SESSION
    DEFAULT_SESSION = Session(access_key=access_key,
                              secret_access_key=secret_access_key)
    DEFAULT_SESSION.auth()


def auth(access, secret):
    """
    Check if a default_session is defined if not call the setup_default_session to create a new session and auth
    If is already defined only call auth again to update keys

    Args:
      access (string): Access Key used to authenticate the user on Sara API
      secret (string): Secret Key used to authenticate the user on Sara API

    Returns:
      Session: return a object of the session class

    Examples:
      >>> result = auth("AKIAIOSFODNN7EXAMPLE", "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY")
      >>> print(result.access_token)
        eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJleGFtcGxlIn0.wqwdbCdHDEoknvUP-kyH2r5NrP4dVdeGeYpEz77MGtc

      Obs: Not valid tokens above, for example purpose only
    """
    if DEFAULT_SESSION is None:
        setup_default_session(access_key=access, secret_access_key=secret)
    else:
        DEFAULT_SESSION.auth()

    return DEFAULT_SESSION
