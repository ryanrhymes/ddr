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
from config import conf, logger
from docker import Client


class Registry():

    def __init__(self, cli):
        self._cli = cli
        self._services = {}
        self.init_service_list()
        pass


    def init_service_list(self):
        """Init the service list."""
        images = self._cli.images()
        for image in images:
            self._services[image['Id']] = image

            # liang: dump the images, need to move to cache abstraction in the future.
            logger.info('dumping %s' % image['Id'])
            if image['Id'] == u'3d3b49d80014e2df3434f282586b3bb2cff0f7b5f58a3e63d9229c48085a53a8':
                continue
            raw = self._cli.get_image(image['Id'])
            tar = open(conf['image_dir']+image['Id']+'.tar', 'w')
            tar.write(raw.data)
            tar.close()
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
    cli = Client(conf['base_url'])
    reg = Registry(cli)
    pass


if __name__=="__main__":
    test()

    sys.exit(0)
