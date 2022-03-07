import sys

from satella.coding.concurrent import TerminableThread
from satella.instrumentation import Traceback

from conqueror.cassandra import session
from conqueror.scraper.get_object_types import get_random_object_type
from conqueror.scraper.orders_obtainer import OrdersObtainer
from conqueror.scraper.scrap_yandex import search_on_yandex
from conqueror.scraper.yandex_api_schema import YandexAPISchema


def run():
    po = OrdersObtainer()
    for i in range(0, int(sys.argv[2])):
        city = po.get_random_city()
        point = po.get_random_point(city)

        utility_point = get_random_object_type()

        query = YandexAPISchema(apikey=sys.argv[1],
                                text=f'{city.city_in_russian} {utility_point}',
                                ll=f'{point[1]},{point[0]}')

        query_d = dict(query)
        points = search_on_yandex(**query_d)

        try:
            for data_point in points['features']:

                if 'CompanyMetaData' not in data_point['properties']:
                    continue
                name = data_point['properties']['name']
                company_id = data_point['properties']['CompanyMetaData']['id']
                geo_lon, geo_lat = data_point['geometry']['coordinates']
                session.execute(
                    'INSERT INTO businesses (sector, businessId, geoLat, geoLon, name) VALUES (%s, %s, %s, %s, %s)',
                    (
                        city.city_in_english,
                        company_id, geo_lat, geo_lon, name
                    ))
        except Exception as e:
            print(Traceback().pretty_format())
        print('Inserted ', len(points['features']), ' data points into Cassandra')
