from channels.generic.websocket import AsyncWebsocketConsumer

import json


class TrafficBroadcast(AsyncWebsocketConsumer):

    msg_type = 'traffic_data'

    async def connect(self):
        await self.channel_layer.group_add(
            self.network_name,
            self.channel_name
        )
        await self.accept()

    def connection_groups(self, **kwargs):
        """
        Called to return the list of groups to automatically add/remove
        this connection to/from.
        """
        return [self.network_name]

    async def receive(self, text=None, bytes=None, **kwargs):
        # Not talking!
        pass

    async def traffic_data(self, event):
        message = event['text']

        # Send message to WebSocket
        await self.send(
                text_data=json.dumps(message))


class SampleNetwork(TrafficBroadcast):
    network_name = "sample_net"
