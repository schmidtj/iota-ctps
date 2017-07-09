""" Configuration options found in ctps.config
      
"""

import time, sys, ConfigParser, io
from tangle import tangle


def main(config):
    t = tangle(config)

    if config.get("iri", 'export_folder'):
        while True:
            t.incremental_read()
            t.print_stats()
            time.sleep(t.resolution)
    if int(config.get("zmq", 'use_zmq')):
        t.continuous_read()


if __name__ == '__main__':
    config = ConfigParser.ConfigParser()
    config.read("ctps.config")
    main(config)
