"""Schema for Yandex places API."""

import dataclasses
import typing as tp


@dataclasses.dataclass
class YandexAPISchema:
    """Provide correct schema to talk with yandex API.

    :param text: Search query, by cit name, business name and so on.
    :param lang: Response language.
    :param apikey: Your api key to yandex places API.
    :param ll: Search area center.
    :param spn: Search area size.
    :param type: Object types:
        - 'geo', toponyms
        - 'biz, businesses
        - 'omitted', automatically detect the type based on the query text
    """
    text: str
    lang: str = "ru_ru"
    apikey: str = "558d43d5-79eb-40c6-938d-e303ab670a3b"
    ll: tp.Optional[str] = ""
    spn: tp.Optional[str] = "0.02,0.02"
    type: tp.Optional[str] = ""
    results: tp.Optional[str] = "500"

    def __iter__(self):
        """Allow to transform dataclass into dict."""
        yield "text", self.text
        yield "lang", self.lang
        yield "apikey", self.apikey
        yield "ll", self.ll
        yield "spn", self.spn
        yield "results", self.results
