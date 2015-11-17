from time import sleep

from conway import Conway

conway = Conway()


def run():
    while True:
        print conway.get_grid()
        conway.iterate()
        sleep(1)

run()
