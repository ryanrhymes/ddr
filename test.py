#!/usr/bin/env python


import httplib
import os
import socket
import sys


def test():
    print "hello"
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server_address = '/var/run/docker.sock'
    sock.connect(server_address)
    pass

def test2():
    server_address = '/var/run/docker.sock'
    conn = httplib.HTTPConnection(server_address)
    conn.request("GET", "/")
    resp = conn.getresponse()

    print resp
    pass


if __name__=="__main__":
    test2()

    sys.exit(0)
