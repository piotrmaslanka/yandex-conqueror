import requests
from satella.coding.decorators import retry


@retry(3, exc_classes=requests.RequestException)
def get_yandex_request(url, arguments) -> dict:
    """
    Return a JSON object querying Yandex at provided parameters.

    Handling CSRF will be done automatically.

    :param url: URL to ask
    :param arguments: dictionary of arguments to add
    :return: object returned via endpoint
    """
    resp = requests.get(url, params=arguments)
    resp.raise_for_status()
    data = resp.json()
    if list(data.keys()) == ['csrfToken']:
        arguments['csrfToken'] = data['csrfToken']
        return get_yandex_request(url, arguments)
    else:
        return data
