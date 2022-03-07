from satella.coding.concurrent import IntervalTerminableThread

from conqueror.scraper.get_object_types import get_random_object_type
from conqueror.scraper.orders_obtainer import OrdersObtainer
from conqueror.scraper.scrap_yandex import search_on_yandex
from conqueror.scraper.yandex_api_schema import YandexAPISchema


class PulseCoordinator(IntervalTerminableThread):
    def __init__(self, po: OrdersObtainer):
        self.po = po
        super().__init__(daemon=True)

    def loop(self):
        city = self.po.get_random_city()
        point = self.po.get_random_point(city)

        utility_point = get_random_object_type()

        query = YandexAPISchema(text=f'{city.city_in_russian} {utility_point}')

        query_d = dict(query)

        points = search_on_yandex(**query_d)
        print(points)
