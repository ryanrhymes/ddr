#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Network abstraction.
#
# Liang Wang @ Computer Lab, Cambridge University
# 2015.06.15


from socket import *
from select import *
from threading import Thread

PORT = 56789

class Network():

    def __init__(self):
        self._udp = socket(AF_INET, SOCK_DGRAM)
        self._udp.bind( ('', 0) )
        self._udp.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

        t = Thread(target=self.start_listen)
        t.start()
        pass


    def broadcast(self, data):
        self._udp.sendto(data, ('<broadcast>', PORT))
        pass


    def start_listen(self):
        s = socket(AF_INET, SOCK_DGRAM)
        s.bind(('<broadcast>', PORT))
        s.setblocking(0)

        while True:
            try:
                result = select([s],[],[])
                msg = result[0][0].recv(1024) 
                print msg
            except KeyboardInterrupt:
                break

    pass
