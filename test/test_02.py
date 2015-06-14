#!/usr/bin/env python

import os
import sys

from docker import Client

def test_1():
    cli = Client(base_url="unix://var/run/docker.sock")
    l = cli.images()

    for d in l:
        print d['RepoTags']
    pass


def test_2():
    cli = Client(base_url="unix://var/run/docker.sock")
    img = cli.get_image('ubuntu')

    tar = open("ubuntu.tar", 'w')
    tar.write(img.data)
    tar.close()
    pass


def test_3():
    cli = Client(base_url="unix://var/run/docker.sock")
    s = cli.pull("busybox")
    print s
    pass


if __name__=="__main__":
    test_1()
    test_3()

    sys.exit(0)
