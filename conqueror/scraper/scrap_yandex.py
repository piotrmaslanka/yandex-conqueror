import requests


def search_for_places(**kwargs: str) -> str:
    """Search for places by text(business desc)."""
    url: str = "https://search-maps.yandex.ru/v1/?"
    r = requests.get(url=url, timeout=5, params={**kwargs}).text
    return r


print(search_for_places
    (
    apikey="4331d83c-3f92-4d0f-bf93-823339e3e71f",
    text="cut,style",
    type="biz",
    lang="en_us",
))
