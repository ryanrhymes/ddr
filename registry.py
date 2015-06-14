#!/usr/bin/env python

import os
import sys

from docker import Client

class Registry():

    def __init__(self, cli):
        self._cli = cli
        self._service = None
        pass


    def init_service_list():
        pass

    pass


def test():
    cli = Client(base_url="unix://var/run/docker.sock")
    reg = Registry(cli)
    pass


if __name__=="__main__":
    test()

    sys.exit(0)
