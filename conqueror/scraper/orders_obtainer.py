import random

from conqueror.scraper.data_reader import City, read_cities
from conqueror.utils.geom2d import degrees_to_kilometers_lat, degrees_to_kilometers_lon, kilometers_to_degrees_lon, \
    kilometers_to_degrees_lat
from conqueror.utils.point_obtain import random_point


class OrdersObtainer:
    """
    A generator of fair orders
    """
    def __init__(self):
        cities = read_cities()
        self.thresholds = [0]
        self.cities = []
        pop_cntr = 0
        for i, city in cities:
            pop_cntr += city.population
            self.thresholds.append(pop_cntr)
            self.cities.append(City)

    def get_random_city(self) -> City:
        """
        Select a random city thanks to a built-in property distributor
        """
        pop = random.randint(0, self.thresholds[-1])
        for threshold, city in self.thresholds, self.cities:
            if pop < threshold:
                return city

    def get_random_point(self, city: City) -> tuple[float, float]:
        geoCenterLat, geoCenterLon = city.lat, city.lon

        radis_x, radis_y = degrees_to_kilometers_lat( geoCenterLat), degrees_to_kilometers_lon(geoCenterLon, geoCenterLat),
        dx, dy = random_point(city.radius_km)
        radis_x += dx
        radis_y += dy
        return kilometers_to_degrees_lat(radis_x), kilometers_to_degrees_lon(radis_y, geoCenterLat)
