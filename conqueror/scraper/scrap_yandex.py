import typing as tp
import requests

# Provide yours API KEY
API_KEY: str = "4331d83c-3f92-4d0f-bf93-823339e3e71f"

search_for_place = {
    "apikey": API_KEY,
    "text": "cut,style",
    "type": "biz",
    "lang": "en_us",
}

# ll (search area center), spn(search area size)
search_for_place_by_ll_spn = {
    "apikey": API_KEY,
    "text": "village of  Pozharishche",
    "ll": "40.17248,60.594641",
    "spn": "3.552069,2.400552",
    "lang": "ru_RU",
}

search_for_business = {
    "apikey": API_KEY,
    "text": "Shear%20Pleasure",
    "type": "biz",
    "lang": "ru_RU",
}


def search_on_yandex(**kwargs: tp.Dict[str, str]) -> str:
    """Search for places | business."""
    url: str = "https://search-maps.yandex.ru/v1/?"
    return requests.get(url=url, timeout=5, params={**kwargs}).text


print(search_on_yandex(**search_for_place_by_ll_spn))
