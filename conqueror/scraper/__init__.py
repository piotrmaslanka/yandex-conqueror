import math
import queue
import threading
from random import random
import time
from satella.coding.concurrent import TerminableThread

from conqueror.scraper.orders_obtainer import OrdersObtainer

API_ENQUIRY_EACH_SECOND = 4     # a query each 4 seconds



def get_fai(lat: float, lon: float, radius: float) -> tuple[float, float]:
    """
    Get a coordinates for a fairly chosen fircle within lat and lon 
    
    :param lat: geo latitude in degrees, + is N
    :param lon: geo longitude in degrees, + is E
    :param radius: radius in kilometres 
    :return: a tuple of (lat, lon)
    """
    radius = 2*math.pi*random()
    u = random()+random()
    if u > 1:
        r = 2-u
    else:
        r = u
    return [r*math.cos(t), r*math.sin(t)]



class PermissionGenerator(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.queue = queue.Queue()

    def run(self):
        while True:
            self.queue.put(1)
            time.sleep(API_ENQUIRY_EACH_SECOND)


class ScrapingThread(TerminableThread):
    def __init__(self, pg: PermissionGenerator):
        super().__init__()
        self.pg = pg

    def run(self):
        while not self._terminating:
            self.pg.queue.get(True)     # obtain the permission to scrape

