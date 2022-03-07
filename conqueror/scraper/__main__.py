import time

from conqueror.scraper.orders_obtainer import OrdersObtainer
from conqueror.scraper.pulse_coordinator import PulseCoordinator


def run():
    pc = PulseCoordinator(OrdersObtainer())
    pc.start()
    time.sleep(100000)


if __name__ == '__main__':
    run()
