from typing import Dict
import json
from sara_sdk.client.requests import fetch
from sara_sdk.common.session import Session
from requests import post

RESOURCE = "metrics"


def retrieve(measurement: str, range: str, filters: Dict, session: Session = None, **kwargs):
    """
    Retrieve a metric by measurement, range and body
    Args:
      measurement (string): Measurement name
      range (string): Measurement range
      body (Dict): A dictionary with the data the will be used on metric
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of metrics
    Returns:
      result (json): returns the result of the request as json
    Example:
      >>> retrieve("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    body = {
        "filters": filters,
        "range": range,
        "measurement": measurement
    }
    result = fetch(method=post, path="{}/{}".format(RESOURCE,
                   measurement), session=session, payload=body, **kwargs)
    return result
