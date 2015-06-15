#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Config contains the basic parameters of DDR system.
#
# Liang Wang @ Computer Lab, Cambridge University
# 2015.06.15


import os
import logging


# set basic paramters
conf = dict()
conf['base_url'] = "unix://var/run/docker.sock"
conf['image_dir'] = "/var/tmp/ddr/"

if not os.path.exists(conf['image_dir']):
    os.makedirs(conf['image_dir'])


# configure logger
logger = logging.getLogger('ddr')
logging.basicConfig(format='%(asctime)s => %(message)s', level=logging.INFO)
