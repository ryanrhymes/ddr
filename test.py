#!/usr/bin/env python


import httplib
import os
import socket
import sys


class Uhttplib(httplib.HTTPConnection):
    """Subclass of Python library HTTPConnection that
    uses a unix-domain socket.
    """

    def __init__(self, path):
        httplib.HTTPConnection.__init__(self, 'localhost')
        self.path = path

    def connect(self):
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.connect(self.path)
        self.sock = sock

    pass


def test():
    print "hello"
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server_address = '/var/run/docker.sock'
    sock.connect(server_address)
    pass


def test2():
    server_address = '/var/run/docker.sock'
    conn = Uhttplib(server_address)
    conn.connect()

    conn.request("GET", "/version")
    conn.request("GET", "/images/json")
    resp = conn.getresponse()

    print resp.read()
    pass


if __name__=="__main__":
    test2()

    sys.exit(0)
