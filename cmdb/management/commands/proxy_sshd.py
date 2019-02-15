# coding=utf-8

# import traceback
# import time
# import json
from django.core.management.base import BaseCommand, CommandError

# from cmdb.models import Host

from cmdb.ssh.sshd import SSHServer
from cmdb.conf import CliSSH

import sys
# /usr/lib64/python2.7/site-packages/sitecustomize.py
reload(sys)
sys.setdefaultencoding('UTF-8')

host = CliSSH['host']  # 监听地址
port = CliSSH['port']


class Command(BaseCommand):
    # 生成SSH服务端，用于透明代理SSH
    help = u'生成SSH透明代理服务器，类似堡垒机功能，使网站支持Xshell终端'

    # def add_arguments(self, parser):
    #     parser.add_argument('port', nargs='?', default='2222', type=int,
    #                         help=u'''
    #                         SSH监听端口，默认为2222
    #                         ''')

    def handle(self, *args, **options):
        # port = options['port']
        ssh_server = SSHServer(host, port)
        ssh_server.run()

