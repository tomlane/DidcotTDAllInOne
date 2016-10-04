#!/usr/bin/env python
import json
import logging


logging.basicConfig()


class Listener(object):

    msg = {}

    def __init__(self, mq):
        self._mq = mq

    def on_message(self, headers, message):

        messageobj = json.loads(message) #converts json to python

        self.msg = messageobj #add it to the msg_list dict for other class visibility

        self._mq.ack(id=headers['message-id'], subscription=headers['subscription']) #ack message

    def on_heartbeat_timeout(self):
      print "Heart beat timeout"

    def on_error(self, headers, body):
      print "error!"
      print headers
      print body

