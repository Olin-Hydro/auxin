from __future__ import absolute_import
from celery import Celery

app = Celery('auxin',
             broker='amqp://jonas:jonas123@localhost/jonas_vhost',
             backend='rpc://',
             include=['auxin.tasks'])