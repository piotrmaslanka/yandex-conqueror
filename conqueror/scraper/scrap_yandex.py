import typing as tp

import requests

from yandex_api_schema import YandexAPISchema


def search_on_yandex(**kwargs: tp.Dict[str, str]):
    """Search for places | business.

    :returns: Json with scraped information about points.
    """
    url: str = "https://search-maps.yandex.ru/v1/?"
    return requests.get(url=url, timeout=5, params={**kwargs}).json()


def extract_point_coordinates(scraped_points) -> None:
    """If it's point, extract coordinates(latitude & longitude)."""
    for feature_key in scraped_points["features"]:
        for geo_key, coordinates in feature_key["geometry"].items():
            if isinstance(coordinates, list):
                latitude, longitude = coordinates[0], coordinates[1]
                print(f"Latitude: {latitude}, Longitude: {longitude}")


scraped_points = search_on_yandex(**dict(YandexAPISchema(text="test")))
extract_point_coordinates(scraped_points)
