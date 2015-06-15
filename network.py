#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Network abstraction.
#
# Liang Wang @ Computer Lab, Cambridge University
# 2015.06.15


from socket import *


PORT = 56789

class Network():

    def __init__(self):
        self._udp = socket(AF_INET, SOCK_DGRAM)
        self._udp.bind( ('', 0) )
        self._udp.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        pass


    def broadcast(self, data):
        self._udp.sendto(data, ('<broadcast>', PORT))
        pass


    pass
