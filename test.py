#!/usr/bin/env python


import os
import socket
import sys


def test():
    print "hello"
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server_address = '/var/run/docker.sock'
    sock.connect(server_address)
    pass


if __name__=="__main__":
    test()

    sys.exit(0)
