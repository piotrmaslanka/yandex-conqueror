import queue
import threading
import time
from satella.coding.concurrent import TerminableThread


API_ENQUIRY_EACH_SECOND = 4     # a query each 4 seconds


def ask(city, item, bbox1, bbox2):



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

