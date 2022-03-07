from conqueror.scraper.pulse_coordinator import PulseCoordinator


def run():
    pc = PulseCoordinator()
    pc.start()


if __name__ == '__main__':
    run()
