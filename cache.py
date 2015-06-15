#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Cache abstraction.
#
# Liang Wang @ Computer Lab, Cambridge University
# 2015.06.15


class Cache():

    def __init__(self, quota):
        """Init the cache."""
        self._quota = quota
        pass


    def add(self):
        """Add a new item to cache."""
        pass


    def remove(self):
        """Remove an item from cache."""
        pass


    def is_full(self):
        """Check if the cache is full."""
        b = False
        return b

    pass
