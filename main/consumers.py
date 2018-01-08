from channels.generic.websockets import WebsocketConsumer


class TrafficBroadcast(WebsocketConsumer):

    # Set to True to automatically port users from HTTP cookies
    # (you don't need channel_session_user, this implies it)
    http_user = True
    strict_ordering = False

    def connection_groups(self, **kwargs):
        """
        Called to return the list of groups to automatically add/remove
        this connection to/from.
        """
        return [self.network_name]

    def receive(self, text=None, bytes=None, **kwargs):
        # Not talking!
        pass


class SampleNetwork(TrafficBroadcast):
    network_name = "sample_net"
