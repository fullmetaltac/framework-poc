from json import dumps, loads
from logging import Logger

from requests import JSONDecodeError, Response


def pprint(value):
    if isinstance(value, bytes):
        value = value.decode("utf-8")

    try:
        value = loads(value)
    except (JSONDecodeError, TypeError):
        return str(value)

    if isinstance(value, (dict, list)):
        return dumps(value, indent=4)
    return str(value)


def log_api(api_logger: Logger, res: Response) -> Response:
    req = res.request
    body = pprint(req.body) if req.body else ""
    api_logger.info(
        "\n-----> [%s] %s\n%s\n<----- [%s %s]\n%s\n",
        req.method,
        req.url,
        body,
        res.status_code,
        res.reason,
        pprint(res.text),
    )
    return res
