#!/usr/bin/env python2.7

import time
from docker import Client
from docker.utils import create_host_config

client = Client(base_url='unix://var/run/docker.sock',version='auto')

def run_image(image_name, port_host, port_container):
    if has_image(image_name) == True:
        config = create_host_config(port_bindings={port_container:port_host})
        container = client.create_container(image=image_name, ports=[port_container], host_config=config)
        client.start(container=container.get('Id'))
        return is_image_running(image_name)
    return False

def has_image(image_name):
    local_images = client.images()
    for image in local_images:
        if image_name in image["RepoTags"]:
            return True
    return False

def pull_image(repo, image_name, wait=True):
    if repo == None: #pull from docker hub
        print 'Pulling image %s from default repo ...' % image_name
        client.pull(image_name, stream=True)
    else:
        print 'Pulling image %s from %s ...' % [image_name, repo]
        client.pull(repo, image_name, stream=True)
    if wait == True:
        timeout = 32
        timeout_step = 1
        while (has_image(image_name) == False and timeout_step <= timeout):
            print 'Waiting %d seconds ...' % timeout_step
            time.sleep(timeout_step)
            timeout_step *= 2
        if timeout_step > timeout:
            print 'Pulling timed out'
        else:
            print 'Pulling finished'
    return has_image(image_name)

def is_image_running(image_name):
    for container in client.containers():
        if container["Image"] == image_name:
            return True
    return False
