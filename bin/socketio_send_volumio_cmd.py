#!/usr/bin/env python
"""
Socket.IO rewrite
WebSocket interface to Volumio Pandora Plugin

Usage:
<this_script.py> <volumio music_service name> <volumio music_service method name> <data as JSON string>

Last Update March 30, 2021
"""

import socketio
import json
import sys
from time import sleep

URL = 'http://volumio.lan:3000'
PANDORA_SERVICE = 'music_service/pandora'
CMD = 'callMethod'
NUM_ARGS = 4 # really 3 arguments

def send_volumio_cmd(payload):
    'Send websocket command to Volumio'

    print('cmd: %s payload: %s' % (CMD, payload))
    sio.connect(URL)
    sio.emit(CMD, payload)
    sleep(5)
    sio.disconnect()


def process_args():
    'Process command-line arguments'

    volumio_payload = {
        'endpoint': '',
        'method': '',
        'data': {}
    }

    if len(sys.argv) > NUM_ARGS:
        print('You have specified too many arguments:\n%s' % sys.argv)
        sys.exit()
    if len(sys.argv) < NUM_ARGS:
        print('You have specified too few arguments:\n%s' % sys.argv)
        sys.exit()

    try:
        volumio_payload['endpoint'] = 'music_service/' + sys.argv[1]
        volumio_payload['method'] = sys.argv[2]
        if isinstance(sys.argv[3], str):
            volumio_payload['data'] = sys.argv[3]
        else:
            volumio_payload['data'] = json.loads(sys.argv[3])

    except Exception as err:
        print('Argument is not a JSON string: %s' % err)
        sys.exit()

    send_volumio_cmd(volumio_payload)
    
sio = socketio.Client() 

process_args() # hit it
