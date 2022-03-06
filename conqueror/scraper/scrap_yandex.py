import typing as tp

import requests

from yandex_api_schema import YandexAPISchema


def search_on_yandex(**kwargs: tp.Dict[str, str]) -> str:
    """Search for places | business."""
    url: str = "https://search-maps.yandex.ru/v1/?"
    return requests.get(url=url, timeout=5, params={**kwargs}).text


print(search_on_yandex(**dict(YandexAPISchema(text="test"))))
