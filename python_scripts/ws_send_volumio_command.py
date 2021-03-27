#!/usr/bin/env python
"""WS interface to Volumio'

Call with </config/ws_send_volumio_command.py> <service> <service_method/procedure> <dataJSON>
'music_service/' is prepended to <service> parameter
i.e. 'music_service/pandora' if <service> == 'pandora'

See https://websockets.readthedocs.io/en/stable/intro.html for WS examples
See https://volumio.github.io/docs/API/WebSocket_APIs.html for Volumio WS API
"""

import sys
import json
import asyncio
import websockets

URI = 'ws://volumio.lan:3000'
PANDORA_SERVICE = 'music_service/pandora'
CMD = 'callMethod'
NUM_ARGS = 4 # really 3 arguments

async def send_volumio_cmd(cmd, payload):
    'Send websocket command to Volumio'

    async with websockets.connect(URI) as websocket:
        await websocket.send(cmd, payload)

        response = await websocket.recv()
        print('response: %s' % response)

async def process_args():
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
        volumio_payload['data'] = json.loads(sys.argv[3])

    except Exception as err:
        print('Argument is not a JSON string: %s' % err)
        sys.exit()

    await send_volumio_cmd(CMD, volumio_payload)

# call process_args() which calls main async function and quits
asyncio.get_event_loop().run_until_complete(process_args())
