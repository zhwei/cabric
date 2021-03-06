# -*- coding: utf-8 -*-

from fabric.api import *
from cabric.env import *

import os


def ez(curr):

    # to specify routes
    # routes = {
    #     'dev': os.path.dirname(__file__) + '/config/cabric/dev.conf',
    #     'beta': os.path.dirname(__file__) + '/config/cabric/beta.conf',
    #     'ol': os.path.dirname(__file__) + '/config/cabric/online.conf',
    # }
    #
    # bind_hosts(curr, routes)

    # create routes auto
    bind_hosts(curr)

    # use cloud feature
    bind_cloud(['pek2', 'CBIWUAKJXMHLLQGYTEXO', 'DqtG1Uf7W7FbiydQje6pTF8PyWXdHubJBPZLtFdY'])
    pass


def hello_fabric():
    local('echo "You can delete this function after initial it."')
    pass


def upgrade(tag=None, clean=False):
    """
    this function must contain `tag` and `clean` options
    :param tag:
    :param clean:
    :return:
    """

    root = '/tmp/cabric'  # repo deploy path
    repo = 'https://github.com/baixing/cabric.git'  # repo demo

    if clean:
        run('rm -rf %s' % root)
        pass

    if ez_env.group == 'ol':
        cmd_git(root, repo, branch='master', tag=tag)
        pass
    elif ez_env.group == 'beta':
        cmd_git(root, repo, branch='beta', tag=tag)
        pass
    elif ez_env.group == 'dev':
        cmd_git(root, repo, branch='dev', tag=tag)
        pass
    else:
        print("[warn]:can't find default config,use master.")
        cmd_git(root, repo, branch='master', tag=tag)
        pass

    pass




















