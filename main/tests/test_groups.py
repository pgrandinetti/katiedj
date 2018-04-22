import pytest

from channels.testing import WebsocketCommunicator
from channels.layers import get_channel_layer

from main.consumers import SampleNetwork

path = '/macro/sample/'


# pytest main/tests/test_groups_channels2.py --ds=main.settings.dev

@pytest.mark.asyncio
async def test_add():
    communicator = WebsocketCommunicator(SampleNetwork, path)
    connected, protocol = await communicator.connect()
    assert connected
    assert await communicator.receive_nothing()
    lay = get_channel_layer()
    await lay.group_send(
            SampleNetwork.network_name,
            {'text': 'ok',
             'type': SampleNetwork.msg_type})
    response = await communicator.receive_json_from()
    assert (response == 'ok')
    assert await communicator.receive_nothing()
    await communicator.disconnect()


@pytest.mark.asyncio
async def test_add_remove():
    communicator = WebsocketCommunicator(SampleNetwork, path)
    connected, protocol = await communicator.connect()
    assert connected
    assert await communicator.receive_nothing()
    lay = get_channel_layer()
    await lay.group_send(
            SampleNetwork.network_name,
            {'text': 'ok',
             'type': SampleNetwork.msg_type})
    response = await communicator.receive_json_from()
    assert (response == 'ok')
    await lay.group_send(
            SampleNetwork.network_name,
            {'text': 'ok',
             'type': SampleNetwork.msg_type})
    await communicator.disconnect()
    assert await communicator.receive_nothing()


@pytest.mark.asyncio
async def test_multi_clients():
    communicator1 = WebsocketCommunicator(SampleNetwork, path)
    connected1, _ = await communicator1.connect()
    assert connected1
    communicator2 = WebsocketCommunicator(SampleNetwork, path)
    connected2, _ = await communicator2.connect()
    assert(connected2)
    assert await communicator1.receive_nothing()
    assert await communicator2.receive_nothing()
    lay = get_channel_layer()
    await lay.group_send(
            SampleNetwork.network_name,
            {'text': 'ok',
             'type': SampleNetwork.msg_type})
    resp1 = await communicator1.receive_json_from()
    resp2 = await communicator2.receive_json_from()
    assert (resp1 == 'ok')
    assert (resp2 == 'ok')
    await communicator1.disconnect()
    await lay.group_send(
            SampleNetwork.network_name,
            {'text': 'ok',
             'type': SampleNetwork.msg_type})
    assert await communicator1.receive_nothing()
    resp2 = await communicator2.receive_json_from()
    await communicator2.disconnect()
    assert (resp2 == 'ok')
