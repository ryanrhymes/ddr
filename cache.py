#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Cache abstraction.
#
# Liang Wang @ Computer Lab, Cambridge University
# 2015.06.15


import time

from config import conf, logger


class Cache():

    def __init__(self):
        """Init the cache."""
        self._root = conf['image_dir']
        self._quota = conf['cache_quota']
        self._cache = {}
        pass


    def add(self, sid):
        """Add a new item to cache."""
        if sid not in self._cache:
            self._cache[sid] = {}
            self._cache[sid]['size'] = 0 # fix
            self._cache[sid]['path'] = '' # fix
            # dumping the image ... not done yet ...
        self.touch(sid)
        pass


    def remove(self, sid):
        """Remove an item from cache."""
        if sid in self._cache:
            del self._cache[sid]
            # delete the image file, not done yet ...
        pass


    def touch(self, sid):
        """Update the timestamp of the content using the current time."""
        self._cache[sid]['timestamp'] = time.time()
        pass


    def is_full(self):
        """Check if the cache is full."""
        used = sum([ v['size'] for v in self._cache.values() ])
        return used >= self._quota

    pass
