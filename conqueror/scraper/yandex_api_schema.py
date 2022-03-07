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
    apikey: str = "161665c4-6a57-4031-ac15-c8abb2dd0808"
    ll: tp.Optional[str] = ""
    spn: tp.Optional[str] = ""
    type: tp.Optional[str] = ""

    def __iter__(self):
        """Allow to transform dataclass into dict."""
        if self.text: yield "text", self.text
        if self.lang: yield "lang", self.lang
        if self.apikey: yield "apikey", self.apikey
        if self.ll: yield "ll", self.ll
        if self.spn: yield "spn", self.spn
        if self.type: yield "type", self.type
