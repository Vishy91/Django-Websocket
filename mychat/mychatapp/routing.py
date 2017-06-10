from channels.routing import route
from . import consumers

channel_routing = {
    'websocket.connect': consumers.ws_connect,
    'websocket.disconnect': consumers.ws_disconnect,
    'websocket.receive': consumers.ws_receive,
}
