#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Registry handles service registration and images transmission.
#
# Liang Wang @ Computer Lab, Cambridge University
# 2015.06.15


import os
import sys

from service import *
from docker import Client


class Registry():

    def __init__(self, cli):
        self._cli = cli
        self._services = None
        self.init_service_list()
        pass


    def init_service_list(self):
        """Init the service list."""
        images = self._cli.images()
        for image in images:
            self._services.append(image)
        pass


    def register_service(self):
        pass


    def unregister_service(self):
        pass


    def get_registry_list(self):
        pass


    def start_service(self):
        pass


    def stop_service(self):
        pass


    def retrieve_service_image(self):
        pass


    def delete_service_image(self):
        pass

    pass


def test():
    cli = Client(base_url="unix://var/run/docker.sock")
    reg = Registry(cli)
    pass


if __name__=="__main__":
    test()

    sys.exit(0)
