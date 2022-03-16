from ..utils.rest import retrieve, list, update, delete, create


def get_robots_by_fleet(fleet, session=None):
    """
    Get a fleet data with the array of robots

    Args:
      fleet (string): Fleet uuid
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json
    """
    result = retrieve("iam/fleets", fleet, session=session)
    return result


def get_robot(robot, session=None):
    """
    Get the robot data

    Args:
      robot (string): Robot uuid
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json
    """
    result = retrieve("iam/robot", robot, session=session)
    return result
