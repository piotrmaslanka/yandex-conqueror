import sys

from satella.coding.concurrent import TerminableThread

from conqueror.cassandra import session
from conqueror.scraper.get_object_types import get_random_object_type
from conqueror.scraper.orders_obtainer import OrdersObtainer
from conqueror.scraper.scrap_yandex import search_on_yandex
from conqueror.scraper.yandex_api_schema import YandexAPISchema


def run():
    for i in range(0, int(sys.argv[2])):
        city = self.po.get_random_city()
        point = self.po.get_random_point(city)

        utility_point = get_random_object_type()

        query = YandexAPISchema(apikey=sys.argv[1],
                                text=f'{city.city_in_russian} {utility_point}',
                                ll=f'{point[0]},{point[1]}')

        query_d = dict(query)
        points = search_on_yandex(**query_d)

        for data_point in points['features']:
            name = data_point['properties']['name']
            company_id = data_point['properties']['CompanyMetaData']['id']
            geo_lon, geo_lat = data_point['geometry']['coordinates']
            session.execute('INSERT INTO businesses (sector, businessId, geoLat, geoLon, name) VALUES (%s, %s, %s, %s, %s)',
                            (
                                city.city_in_english,
                                company_id, geo_lat, geo_lon, name
                            ))

        print('Inserted %s data points into Cassandra', len(points['features']))
