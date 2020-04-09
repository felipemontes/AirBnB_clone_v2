#!/usr/bin/python3
from fabric.api import *

env.hosts = ['35.196.60.116', '54.221.176.56']
env.user = 'ubuntu'


def do_clean(number=0):
    """ deletes out of data archives """

    number = int(number)
    if number == 1 or number == 0:
        local('cd versions; ls | head -n -1 | xargs rm -rf')
        run('cd /data/web_static/releases; ls | head -n -1 | xargs rm -rf')
    elif number == 2:
        local('cd versions; ls | head -n -2 | xargs rm -rf')
        run('cd /data/web_static/releases; ls | head -n -2 | xargs rm -rf')
