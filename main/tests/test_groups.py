from channels import Group
from main.consumers import SampleNetwork

from channels.test import ChannelTestCase, WSClient


class TestGroupSampleNet(ChannelTestCase):

    path = '/macro/sample/'

    def test_add(self):
        client = WSClient()
        client.send_and_consume('websocket.connect', path=self.path)
        self.assertIsNone(client.receive())
        Group(SampleNetwork.network_name).send(
            {'text': 'ok'}, immediately=True)
        self.assertEqual(client.receive(json=False), 'ok')

    def test_add_remove(self):
        client = WSClient()
        client.send_and_consume('websocket.connect', path=self.path)
        self.assertIsNone(client.receive())
        Group(SampleNetwork.network_name).send(
            {'text': 'ok'}, immediately=True)
        self.assertEqual(client.receive(json=False), 'ok')
        client.send_and_consume('websocket.disconnect', path=self.path)
        Group(SampleNetwork.network_name).send(
            {'text': 'ok'}, immediately=True)
        self.assertIsNone(client.receive())

    def test_multi_clients(self):
        client1 = WSClient()
        client2 = WSClient()
        client1.send_and_consume('websocket.connect', path=self.path)
        self.assertIsNone(client1.receive())
        client2.send_and_consume('websocket.connect', path=self.path)
        self.assertIsNone(client2.receive())
        Group(SampleNetwork.network_name).send(
            {'text': 'ok'}, immediately=True)
        self.assertEqual(client1.receive(json=False), 'ok')
        self.assertEqual(client2.receive(json=False), 'ok')
        client1.send_and_consume('websocket.disconnect', path=self.path)
        Group(SampleNetwork.network_name).send(
            {'text': 'ok'}, immediately=True)
        self.assertIsNone(client1.receive())
        self.assertEqual(client2.receive(json=False), 'ok')
