from flask import Response
from satella.json import json_encode
from satella.coding import wraps


def as_json(fun):
    """
    Functions decorated with this are expect to return one of three positions:

    * None - HTTP 204 will be sent
    * tuple/2 - tuple[0] will contain the response and tuple[1] will contain the status code
    * other things - HTTP 200 will be returned

    Every dict and list returned will be stringified with Satella's stringify
    """
    @wraps(fun)
    def outer(*args, **kwargs):
        data = fun(*args, **kwargs)
        if data is None:
            status_code, content_type = 204, None
        else:
            content_type = 'application/json'
            if isinstance(data, tuple):
                if len(data) == 2:
                    data, status_code = data
            else:
                status_code = 200
            data = json_encode(data)

        return Response(data, status=status_code, content_type=content_type)

    return outer
